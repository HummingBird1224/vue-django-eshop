# canal

## URLs
* canal: `localhost` + `port:8000`
* 管理画面: `/canal-admin/`
* rest_framework: `canal-api-auth/`
* dev: `canal/urls_dev.py`
* production: `canal/urls.py`

## Commands
マイグレーション (Requires Mysql server started)
```bash
python manage.py migrate
```

最初にmysqlとの互換性を確かめる
```bash
python manage.py check
```
^ここ読んでね^
^https://django-mysql.readthedocs.io^

サーバー立ち上げ
```buildoutcfg
python manage.py runserver
celery -A canal worker -l info
```


*for development*
マイグレーションファイル作成
```bash
python manage.py makemigration
```


**注意**
- DB名、ユーザーネーム、パスは環境変数に
- テストする際は別DBで試してください
- `sqlmigrate [アプリ名]`でsqlを表示できやす
- マイグレーションできない場合は↑で表示したsqlを直打ちしてください（Tips参照）


## フロントエンドの環境構築
```
make setup_frontend
```

## SVGについて
canalでは、svgファイルをひとまとめのインラインsvgにして、useタグで使い回せるような仕組みが用意されています。

### 環境構築
```
make setup_svg
```

### 使い方
1. svg ディレクトリにsvgファイルを追加する。
2. 追加したsvgファイルの中で色の指定を行っている記述を削除する（style属性）
3. `make gen_svg_sprites` を実行する。

↑の作業を行うと、ひとまとめになったインラインsvgが `src/templates/svg.html` に吐き出されます。

## Tips

### Djangoのマイグレーションで詰まったら

- SQLが実行されていない場合
```code:sh
python manage.py sqlmigrate [app_name] [migration_id ex.0001]
```
で生のsqlを吐いてくれるので、それをDBに直接打ち込む。


### Loginに関して

Loginには二種類ある。
- 通常のLogin画面からのログイン
- 確認メールのリンクを押した際の自動ログイン
通常のLoginは`accounts.views.CartMergingLoginView`の中でログイン作業をしている。
確認メールから（初回登録時のみ）は`accounts.adapter.CustomAccountAdapter`の`login`中で行なっている。
Loginでは、
- カートのマージ
- セッション中のorderの更新
をしないといけない


### Cart/Orderに関して
cartはsession中に`cart`というキーでIDを保存している。
orderはsession中に`order`というキーで注文番号が保存されている。

////////////