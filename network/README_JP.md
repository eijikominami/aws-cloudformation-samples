[**English**](README.md) / 日本語

# CloudFormation Template - Network

これは、**AWSのネットワークサービス** に関するサンプルテンプレートです。

```bash
.
├── templates/                  <-- テンプレートファイル
├── README_JP.md                <-- この導入ガイド
└── README.md                   <-- 導入ガイド（英語版）
```

## クイックスタート

以下のボタンをクリックして **デプロイを開始** してください。

[![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/create/review?stackName=VPNSample&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-samples/network/vpn.yaml)

## デプロイ

以下のコマンドを実行してテンプレートをデプロイしてください。

```bash
aws cloudformation deploy --template-file template.yaml --stack-name VPNSample --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND
```

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](images/architecture.png)