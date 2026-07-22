[**English**](README.md) / 日本語

# CloudFormation テンプレート - Analytics

``Amazon Quick (QuickSight)`` に関するサンプルテンプレートです。

```bash
.
├── sources/                    <-- ソースファイル (index.html)
├── templates/                  <-- テンプレートファイル
├── README_JP.md                <-- この説明ファイル
└── README.md                   <-- 説明ファイル（英語）
```

## 前提条件

デプロイの前に以下を準備してください。

- 匿名埋め込みが有効化済みの Amazon Quick Enterprise エディションのサブスクリプション
- Amazon Quick アカウントで `quicksight:GenerateEmbedUrlForAnonymousUser` 権限を持つ IAM ロール
- その IAM ロールの信頼ポリシーで、デプロイ先アカウントからの `sts:AssumeRole` を許可していること

## TL;DR

以下のボタンをクリックすることで、CloudFormation をデプロイすることが可能です。

| テンプレート名 | AWS リージョン | 起動 |
| --- | --- | --- |
| Amazon Quick Anonymous Embedding | ap-northeast-1 | [![cloudformation-launch-stack](images/cloudformation-launch-stack.png)](https://console.aws.amazon.com/cloudformation/home?region=ap-northeast-1#/stacks/quickcreate?stackName=Quick-Embedding&templateURL=https://eijikominami.s3-ap-northeast-1.amazonaws.com/aws-cloudformation-samples/analytics/quick-anonymous-embedding.yaml) |

## デプロイ

必要なパラメータを指定してコマンドを実行します。

```bash
aws cloudformation deploy \
  --template-file templates/quick-anonymous-embedding.yaml \
  --stack-name Quick-Embedding \
  --capabilities CAPABILITY_NAMED_IAM \
  --parameter-overrides \
    QuickAccountId=123456789012 \
    QuickEmbeddingRoleArn=arn:aws:iam::123456789012:role/QuickEmbeddingForWebApp \
    DashboardId=your-dashboard-id
```

オプションのパラメータは以下の通りです。

| 名前 | タイプ | デフォルト値 | 必須 | 詳細 |
| --- | --- | --- | --- | --- |
| DashboardId | String | | ○ | 埋め込む Amazon Quick ダッシュボード ID |
| Namespace | String | default | | Amazon Quick の匿名埋め込み用 Namespace |
| QuickAccountId | String | | ○ | Amazon Quick が設定されている AWS アカウント ID |
| QuickEmbeddingRoleArn | String | | ○ | Amazon Quick アカウントで AssumeRole する IAM ロール ARN |
| QuickRegion | String | us-east-1 | | ダッシュボードがデプロイされている AWS リージョン |

## デプロイ後の手順

スタック作成後に以下を実施してください。

1. Outputs に記載の S3 バケットに `index.html` をアップロード
2. Outputs に記載の CloudFront ドメインを Amazon Quick の allowed domain として登録
3. コンテンツ更新時は CloudFront キャッシュを無効化: `aws cloudfront create-invalidation --distribution-id <ID> --paths "/*"`
