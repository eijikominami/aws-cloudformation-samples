English / [**日本語**](README_JP.md)

# CloudFormation template - Media

これは、**IoT** に関するサンプルテンプレートです。

```bash
.
├── templates/                  <-- テンプレートファイル
├── README_JP.md                <-- この導入ガイド
└── README.md                   <-- 導入ガイド（英語版）
```

## クイックスタート

以下のボタンをクリックして **デプロイを開始** してください。

| テンプレート名 | リージョン | 実行 |
| --- | --- | --- |
| AWS IoT 1-Click | ap-northeast-1 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/quickcreate?stackName=IoT-1Click&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-samples/iot/iot-1click.yaml) |

## デプロイ

以下のコマンドを実行してテンプレートをデプロイしてください。

```bash
aws cloudformation deploy --template-file iot-1click.yaml --stack-name IoT-1Click --capabilities CAPABILITY_NAMED_IAM
```

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](images/architecture-iot-1click.png)