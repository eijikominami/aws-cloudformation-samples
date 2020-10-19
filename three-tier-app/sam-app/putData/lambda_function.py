import base64
import json
import boto3
import os
import copy
# Lambda Powertools
from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer

# DynamoDB オブジェクト
dynamodb = boto3.resource('dynamodb')
# DynamoDB Table オブジェクト
# 環境変数の読み取り
table = dynamodb.Table(os.environ['DATA_DB_NAME'])

user_id_key_name = 'user_id'
group_id_key_name = 'group_id'
attributes_key_name = 'attributes'

# Lambda Powertools
logger = Logger()
tracer = Tracer()

@logger.inject_lambda_context(log_event=True)
@tracer.capture_lambda_handler
def lambda_handler(event, context):

    """
    Kinesis からデータを取得して、DynamoDBに書き込みます。

    Parameters
    ----------
    event : event
        イベントデータ
    context : LambdaContext
        コンテクスト
    """

    records = decode_records(event)
    for record in records:
        user_id = record['data'][user_id_key_name]
        group_id = record['data'][group_id_key_name]
        attributes = copy.deepcopy(record['data'])
        del attributes[user_id_key_name]
        del attributes[group_id_key_name]
        update_data(user_id, group_id, attributes)

def update_data(user_id, group_id, attributes):

    """
    UpdateItem メソッドを用いて DynamoDB を更新します。

    Parameters
    ----------
    user_id : string
        ユーザID
    group_id : string
        グループID
    attributes : map
        属性データ

    Returns
    -------
    succeed : bool
        更新に成功すると true を返す
    """

    try:
        # Sort an array of voting 
        response = table.update_item(
            Key={
                user_id_key_name:user_id,
                group_id_key_name:group_id
            },
            UpdateExpression="SET #attr = :attr",
            ExpressionAttributeNames={
                '#attr': attributes_key_name
            },
            ExpressionAttributeValues={
                ':attr': attributes
            }
        )
        logger.structure_logs(append=True, dynamodb_response=response)
        logger.debug("Published a dynamodb query.")
        return True
    except Exception:
        return False

def decode_records(event):

    """
    インベントレコードをBase64デコードします。

    Parameters
    ----------
    event : event
        イベントデータ

    Returns
    -------
    decoded_records : string
        デコード済みのイベントレコード
    """

    records = []
    
    for record in event['Records']:
        # Base64デコード
        payload = base64.b64decode(record['kinesis']['data']).decode('utf-8')
        records.append({"data": json.loads(payload), "approximateArrivalTimestamp": str(int(record['kinesis']['approximateArrivalTimestamp']))})
    return records