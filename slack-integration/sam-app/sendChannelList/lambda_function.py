import boto3
import json
import logging
import os
import sys
# Lambda Powertools
from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer

import base64
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

# Lambda Powertools
logger = Logger()
tracer = Tracer()

@logger.inject_lambda_context(log_event=True)
@tracer.capture_lambda_handler
def lambda_handler(event, context):

    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    TEXT = os.environ['TEXT']
    HOOK_URL = os.environ['HOOK_URL']
    if os.environ['ENCRYPT'] == 'true':
        # The base-64 encoded, encrypted key (CiphertextBlob) stored in the ACCESS_TOKEN and HOOK_URL environment variable
        ACCESS_TOKEN = boto3.client('kms').decrypt(CiphertextBlob=base64.b64decode(ACCESS_TOKEN))['Plaintext'].decode('utf-8')
        HOOK_URL = boto3.client('kms').decrypt(CiphertextBlob=base64.b64decode(HOOK_URL))['Plaintext'].decode('utf-8')
    # Sends Slack
    sendMessage(event, HOOK_URL, createMessage(TEXT, ACCESS_TOKEN))

def createMessage(TEXT, ACCESS_TOKEN):
    
    team_response = urlopen(Request("https://slack.com/api/team.info?token=" + ACCESS_TOKEN))
    team = json.loads(team_response.read().decode('utf8'))['team']
    
    channel_response = urlopen(Request("https://slack.com/api/conversations.list?token=" + ACCESS_TOKEN))
    channels = json.loads(channel_response.read().decode('utf8'))['channels']
    
    attachments = []
    for channel in channels:
        if channel['purpose']['value']:
            attachment = {
                'title': '#' + channel['name'],
                'title_link': 'slack://channel?team=' + team['id'] + '&id=' + channel['id'],
                'text':  '#' + channel['name'] + ' は、「' + channel['purpose']['value'] + '」に関するチャンネルです。',
                'footer': str(channel['num_members']) + '人参加'
                }
            attachments.append(attachment)
    
    return {
        'text': TEXT,
        'attachments': attachments
    }

def sendMessage(event, hook_url, message):
        
    try:
        # Sends message
        if not hook_url or message is None:
            logger.info("Hook url or message is empty.")
        else:
            req = Request("https://" + hook_url, json.dumps(message).encode('utf-8'))
            try:
                logger.structure_logs(append=True, slack_hook_url=hook_url)
                logger.info("Posted a message to Slack.")
                response = urlopen(req)
                response.read()
            except HTTPError:
                logger.exception("Received an exception in %s.", sys._getframe().f_code.co_name)
            except URLError:
                logger.exception("Received an exception in %s.", sys._getframe().f_code.co_name)                                    
    except json.decoder.JSONDecodeError:
        logger.info("Message is NOT a JSON format.")