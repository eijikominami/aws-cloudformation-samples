English / [**日本語**](README_JP.md)

# CloudFormation Template - Network

This is a sample template about network services on AWS.

```bash
.
├── templates/                  <-- template files
├── README_JP.md                <-- Instructions file (Japanese)
└── README.md                   <-- This instructions file
```

## QuickStart

Click the following button to deploy the project.

[![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=VPNSample&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-samples/network/vpn.yaml)

## Packaging and deployment

Run the following command to deploy the template.

```bash
aws cloudformation deploy --template-file template.yaml --stack-name VPNSample --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

## Architecture

The following sections describe the individual components of the architecture.

![](images/architecture.png)