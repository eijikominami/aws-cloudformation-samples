# sam-app

This is a sample template to **monitor serverless services** .

```bash
.
├── apigateway-get.yaml         <-- SAM Template for Amazon API Gateway
├── apigateway-post.yaml        <-- SAM Template for Amazon API Gateway
├── apigateway.yaml             <-- SAM Template for Amazon API Gateway
├── dynamodb-throttle.yaml      <-- SAM Template for Amazon DynamoDB
├── dynamodb.yaml               <-- SAM Template for Amazon DynamoDB
├── kinesis.yaml                <-- SAM Template for Amazon Kinesis Streams
├── lambda.yaml                 <-- SAM Template for AWS Lambda
├── README.md                   <-- Instructions file (Japanese)
├── README_EN.md                <-- This instructions file
├── sendSlackMessage            <-- Source code for a lambda function
│   ├── lambda_function.py      <-- Lambda function code
│   └── requirements.txt        <-- Lambda function code
└── template.yaml               <-- SAM Template
```

This template sets Amazon CloudWatch Alarms for the following services and creates related resources.

+ **Amazon API Gateway**
+ **Amazon DynamoDB**
+ **Amazon Kinesis Streams**
+ **AWS Lambda**

## Packaging and deployment

Firstly, we need a `S3 bucket` where we can upload our Lambda functions packaged as ZIP before we deploy anything - If you don't have a S3 bucket to store code artifacts then this is a good time to create one:

```bash
aws s3 mb s3://BUCKET_NAME
```

Next, run the following command to build Lambda source codes and generate deployment artifacts:

```bash
sam build
```

Next, run the following command to package our Lambda function to S3:

```bash
sam package --output-template-file packaged.yaml --s3-bucket BUCKET_NAME
```

Next, the following command will create a Cloudformation Stack and deploy your SAM resources.

```bash
aws cloudformation deploy --template-file packaged.yaml --stack-name Monitoring --s3-bucket BUCKET_NAME --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```