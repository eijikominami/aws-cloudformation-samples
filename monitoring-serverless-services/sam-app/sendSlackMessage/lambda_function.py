import boto3
import json
import logging
import os
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

SLACK_HOOK_URL = os.environ['SLACK_HOOK_URL']
SLACK_CHANNEL = os.environ['SLACK_CHANNEL_NAME']
HOOK_URL = "https://" + SLACK_HOOK_URL

logger = logging.getLogger()
logger.setLevel(logging.INFO)

@xray_recorder.capture('lambda_handler')
def lambda_handler(event, context):

    warning = {"alarm_prefix": "Warning", "color": "danger", "title": "異常内容"}
    notice  = {"alarm_prefix": "Notice", "color": "warning", "title": "警告内容"}

    logger.info("Event: " + str(event))
    
    try:
        message = json.loads(event['Records'][0]['Sns']['Message'])

        if 'AlarmName' in message:

            alarm_name = message['AlarmName']
            alarm_description = message['AlarmDescription']
            new_state = message['NewStateValue']
            reason = message['NewStateReason']

            if new_state == "OK":
                slack_message = {
                    'channel': SLACK_CHANNEL,
                    'text': "異常/警告状態から *回復しました* 。",
                    'attachments': [{
                        'color': "good",
                        'fields': [
                                {
                                    'title': "メトリクス",
                                    'value': "%s" % (alarm_name)
                                },
                                {
                                    'title': "現在の状態",
                                    'value': "%s" % (new_state)
                                }
                            ]
                    }]
                }
            else: 
                # Alert level
                if alarm_name.startswith(warning["alarm_prefix"]):
                    color = warning["color"]
                    title = warning["title"]
                elif alarm_name.startswith(notice["alarm_prefix"]):
                    color = notice["color"]
                    title = notice["title"]
                else:
                    color = "Danger"
                    title = "不明なエラー"
                # Message body
                slack_message = {
                    'channel': SLACK_CHANNEL,
                    'text': "%s" % (alarm_description),
                    'attachments': [{
                        'color': color,
                        'fields': [
                                {
                                    'title': title,
                                    'value': "%s state is now %s" % (alarm_name, new_state)
                                },
                                {
                                    'title': "発生原因",
                                    'value': "%s" % (reason)
                                }
                            ]
                    }]
                }
        else:
            slack_message = None
    except json.decoder.JSONDecodeError as e:
        slack_message = None
    # Sends Slack
    if slack_message is not None:
        req = Request(HOOK_URL, json.dumps(slack_message).encode('utf-8'))
        try:
            response = urlopen(req)
            response.read()
        except HTTPError as e:
            logger.error("Request failed: %d %s", e.code, e.reason)
        except URLError as e:
            logger.error("Server connection failed: %s", e.reason)