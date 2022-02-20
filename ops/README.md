English / [**日本語**](README_JP.md)

# CloudFormation template - Ops

This is a sample template about ops/automation about Amazon EC2.

```bash
.
├── templates/                  <-- template files
├── README_JP.md                <-- Instructions file (Japanese)
└── README.md                   <-- This instructions file
```

## QuickStart

Click the following button to deploy the project.

[![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=EC2Ops&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-samples/ops/ec2.yaml)

## Packaging and deployment

Run the following command to deploy the template.

```bash
aws cloudformation deploy --template-file template.yaml --stack-name EC2Ops --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

## Architecture

The following sections describe the individual components of the architecture.

![](images/architecture.png)