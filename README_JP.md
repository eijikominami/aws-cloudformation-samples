[**English**](README.md) / 日本語

# AWSCloudFormationSamples
![GitHub Stars](https://img.shields.io/github/stars/eijikominami/aws-cloudformation-samples.svg?style=social&label=Stars)
![GitHub](https://img.shields.io/github/license/eijikominami/aws-cloudformation-samples)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/eijikominami/aws-cloudformation-samples)

AWSCloudFormationSamples は、Cloudformationテンプレートのサンプル集です。

## Templates

本プロジェクトは、以下のサンプルプログラムを含んでいます。

| テンプレート名 | リージョン | 実行 |
| --- | --- | --- |
| [IoT](/iot/README_JP.md) | ap-northeast-1 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/quickcreate?stackName=IoT-1Click&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-samples/iot/iot-1click.yaml) |
| [Media](/media/README_JP.md) | ap-northeast-1 | |
| [Video Analysis Pipeline](/video-analysis-stepfunctions/README_JP.md) | ap-northeast-1 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=video-analysis-stepfunctions&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-samples/video-analysis-stepfunctions/template.yaml) |
| [Network](/network/README_JP.md) | ap-northeast-1 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=VPNSample&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-samples/network/vpn.yaml) |
| [EC2 Ops/Automation](/ops/README_JP.md) | ap-northeast-1 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=EC2Ops&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-samples/ops/ec2.yaml) |
| Three Tier App | ap-northeast-1 | [CloudFormation](/three-tier-app/templates/README_JP.md) / [SAM](/three-tier-app/sam-app/README_JP.md)|

## Architecture

The following section describes the individual components of the architecture.

### IoT

![](iot/images/architecture-iot-1click.png)

### Media

![](media/images/architecture-ivs-s3-cloudfront.png)

![](media/images/architecture-medialive-mediapackage.png)

![](media/images/architecture-medialive-mediastore.png)

![](media/images/architecture-medialive-s3.png)

### Network

![](network/images/architecture.png)

### CloudOps

![](ops/images/architecture.png)

### Three tier application

![](three-tier-app/images/architecture.png)