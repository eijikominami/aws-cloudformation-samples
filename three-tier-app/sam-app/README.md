# sam-app

これは、`AWS SAM` 向けの **3層アプリケーション** のサンプルテンプレートです。

```bash
.
├── README.md                   <-- この導入ガイド
├── README_EN.md                <-- この導入ガイド（英語版）
├── getData                     <-- Lambda用ディレクトリ
│   ├── lambda_function.py      <-- メイン関数
│   └── requirements.txt        <-- ライブラリの依存関係
├── putData                     <-- Lambda用ディレクトリ
│   ├── lambda_function.py      <-- メイン関数
│   └── requirements.txt        <-- ライブラリの依存関係
└── template.yaml               <-- SAMテンプレート
```

## クイックスタート

以下のURLの **Deploy** ボタンをクリックして **デプロイを開始** してください。

+ [three-tier-app-sample
](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-east-1:172664222583:applications~three-tier-app-sample)

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
aws cloudformation deploy --template-file packaged.yaml --stack-name ThreeTierApp-SAM --s3-bucket BUCKET_NAME --capabilities CAPABILITY_NAMED_IAM
```

## アーキテクチャ

このテンプレートが作成するAWSリソースのアーキテクチャ図は、以下の通りです。

![](../images/architecture.png)

## APIリファレンス

この API エンドポイントは、 `User` メソッドのみを有しています。

### POST /user

`user_id`　と関連するデータを登録します。

#### パラメータ

`user_id` と `grouo_id` は必須です。また、任意のキーバリュー値追加することができます。

```json
{
    "user_id": "string",
    "group_id": "string",
    "KEY": "VALUE"
}
```

#### レスポンス

| レスポンスコード | 内容 |
| --- | --- |
| 200 | 登録完了 |
| 400 | 不正な入力データ |
| 500 | 内部サーバエラー |

### GET /user/{user_id}

ユーザデータを取得します。

#### レスポンス

| レスポンスコード | 内容 |
| --- | --- |
| 200 | OK |
| 500 | 内部サーバエラー |

```json
{
    "user_id": "string",
    "group_id": "string",
    "KEY": "VALUE"
}
```