# sam-app

これは、**サーバレスサービスの監視設定を行う** SAMサンプルテンプレートです。

```bash
.
├── apigateway-get.yaml         <-- Amazon API Gateway 用のSAMテンプレート
├── apigateway-post.yaml        <-- Amazon API Gateway 用のSAMテンプレート
├── apigateway.yaml             <-- Amazon API Gateway 用のSAMテンプレート
├── dynamodb-throttle.yaml      <-- Amazon DynamoDB 用のSAMテンプレート
├── dynamodb.yaml               <-- Amazon DynamoDB 用のSAMテンプレート
├── kinesis.yaml                <-- Amazon Kinesis Streams 用のSAMテンプレート
├── lambda.yaml                 <-- AWS Lambda 用のSAMテンプレート
├── README.md                   <-- この導入ガイド
├── README_EN.md                <-- この導入ガイド（英語版）
├── sendSlackMessage            <-- Lambda用ディレクトリ
│   ├── lambda_function.py      <-- メイン関数
│   └── requirements.txt        <-- ライブラリの依存関係
└── template.yaml               <-- SAMテンプレート
```

このテンプレートは、以下のAWSサービスならびに関連するサービスに関する `CloudWatch` を作成します。

+ **Amazon API Gateway**
+ **Amazon DynamoDB**
+ **Amazon Kinesis Streams**
+ **AWS Lambda**

## デプロイ

まず、Zip化されたLambda関数をアップロード可能な `S3バケット` を用意します。もし、S3バケットが存在しない場合は、以下のコマンドを実行してください。

```bash
aws s3 mb s3://BUCKET_NAME
```

次に、Lambdaをビルドし、アーティファクトを生成するために、以下のコマンドを実行します。

```bash
sam build
```

次に、LambdaをS3バケットに置くために、以下のコマンドを実行します。

```bash
sam package --output-template-file packaged.yaml --s3-bucket BUCKET_NAME
```

以下のコマンドを実行すると、CloudFormationスタックが生成され、SAMリソースがデプロイされます。

```bash
aws cloudformation deploy --template-file packaged.yaml --stack-name Monitoring --s3-bucket BUCKET_NAME --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```