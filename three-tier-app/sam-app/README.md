English / [**日本語**](README_JP.md)

# sam-app

This is a sample template of a **three tier application** for `sam-app`.

```bash
.
├── README_JP.md                <-- Instructions file (Japanese)
├── README.md                   <-- This instructions file
├── getData                     <-- Source code for a lambda function
│   ├── lambda_function.py      <-- Lambda function code
│   └── requirements.txt        <-- Lambda function code
├── putData                     <-- Source code for a lambda function
│   ├── lambda_function.py      <-- Lambda function code
│   └── requirements.txt        <-- Lambda function code
└── template.yaml               <-- SAM Template
```

## Quick Start

Refer to the following link and click the **Deploy** button.

+ [three-tier-app-sample
](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~three-tier-app-sample)

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
aws cloudformation deploy --template-file packaged.yaml --stack-name ThreeTierApp-SAM --s3-bucket BUCKET_NAME --capabilities CAPABILITY_NAMED_IAM
```

## Architecture

The following sections describe the individual components of the architecture.

![](../images/architecture.png)

## API Rerefence

The endpoint only has `User` method. 

### POST /user

Register `user_id` and related data.

#### Parameters

`user_id` and `grouo_id` are required. Any key-value data can be added in the body.

```json
{
    "user_id": "string",
    "group_id": "string",
    "KEY": "VALUE"
}
```

#### Response Messages

| Response Code | Details |
| --- | --- |
| 200 | Registered. |
| 400 | Invalid request body. |
| 500 | Internal server error. |

### GET /user/{user_id}

Get user information.

#### Response Messages

| Response Code | Details |
| --- | --- |
| 200 | OK. |
| 500 | Internal server error. |

```json
{
    "user_id": "string",
    "group_id": "string",
    "KEY": "VALUE"
}
```