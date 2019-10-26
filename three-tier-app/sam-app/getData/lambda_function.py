import json
import boto3
import os
from boto3.dynamodb.conditions import Key, Attr
# AWS X-Ray SDK for Python
from aws_xray_sdk.core import xray_recorder
from aws_xray_sdk.core import patch

# DynamoDB オブジェクト
dynamodb = boto3.resource('dynamodb')
# DynamoDB Table オブジェクト
# 環境変数の読み取り
table = dynamodb.Table(os.environ['DATA_DB_NAME'])

user_id_key_name = 'user_id'

@xray_recorder.capture('lambda_handler')
def lambda_handler(event, context):

    """
    リクエストに応じたJSONファイルをAPI Gatewayに返します。

    Parameters
    ----------
    event : event
        イベントデータ
    context : LambdaContext
        コンテクスト
    """

    user_id = event['pathParameters'][user_id_key_name]
    try:
        # JSON値を取得
        body = get_data(user_id)
        
        # CROS対応
        # Decimal型をfloat型に変換
        return {
            'statusCode': 200,
            'headers': { 
                        "Access-Control-Allow-Origin" : os.environ['ACCESS_CONTROL_ALLOW_ORIGIN'],
                        "Access-Control-Expose-Headers": os.environ['ACCESS_CONTROL_EXPOSE_HEADERS']
                    },
            'body':  json.dumps(body, default=decimal_default_proc)
        }
    except Exception as e:
        return create_error_response(500, str(e))

@xray_recorder.capture('get_data')
def get_data(user_id):

    """
    DynamoDB からデータを取得します。

    Parameters
    ----------
    user_id : string
        ユーザID

    Returns
    -------
    json : string
        取得したJSONデータ
    """

    response = table.query(
        KeyConditionExpression=Key(user_id_key_name).eq(user_id)
    )
    if 'Items' not in response:
        return None
    else:
        return response['Items']

@xray_recorder.capture('create_error_response')
def create_error_response(status_code, message):

    """
    エラーレスポンスを生成します。

    Parameters
    ----------
    status_code : int
        ステータスコード
    message : string
        メッセージ

    Returns
    -------
    json : string
        生成したJSONデータ
    """

    return {
        'statusCode': status_code,
        'headers': { 
            "Access-Control-Allow-Origin" : os.environ['ACCESS_CONTROL_ALLOW_ORIGIN'],
            "Access-Control-Expose-Headers": os.environ['ACCESS_CONTROL_EXPOSE_HEADERS']
        },
        'body': '{"message": "' + message + '"}'
    }

@xray_recorder.capture('decimal_default_proc')
def decimal_default_proc(obj):

    """
    Decimal 型を float 型に変換します。

    Parameters
    ----------
    obj : Decimal
        入力値

    Returns
    -------
    obj : float
        型変換後の値
    """

    from decimal import Decimal
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError