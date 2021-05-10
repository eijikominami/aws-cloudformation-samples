English / [**日本語**](README_JP.md)

# CloudFormation Template - Three Tier App

This is a sample template of a **three tier application** for `CloudFormation`.

```bash
.
├── templates/                  <-- template files
├── README_JP.md                <-- Instructions file (Japanese)
└── README.md                   <-- This instructions file
```

## QuickStart

Click the following button to deploy the project.

[![cloudformation-launch-stack](../images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/new?stackName=ThreeTierApp-CFn&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-samples/three-tier-app/template.yaml)

## Packaging and deployment

Run the following command to deploy the template.

```bash
aws cloudformation deploy --template-file template.yaml --stack-name ThreeTierApp-CFn --capabilities CAPABILITY_NAMED_IAM
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