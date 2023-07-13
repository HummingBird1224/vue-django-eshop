# 商品に関して

モデル（`products/models.py`）参照

基本は、
- 名前
- スラグ
- カテゴリ
- ユースケース(カテゴリのようなもの)
- タグ
- 説明文
によって構成される。

その他情報は`extra_info`フィールドに保存する

原価計算周りで必要な情報は
`price_type`と`price_params`に保存される
ただし`price_type`は今後消すかも
`price_params`の中に
原価計算に必要なパラメータや
カートに入れるときに必要なパラメータがはいっている。
（カートに入れる際に必要なパラメータは原価計算と関係ないものもあるので注意）


`extra_info`が持ちうる値は`product_data`内の各商品のjsonデータを参照
jsonデータはDBにあくまでも入れれるデータであり、
これらのファイルをサーバープログラムは参照することはない。

商品をカートに入れる（原価計算をする）際に必要なパラメータは
- height
- depth
- width
- color_num
- quantity

- outside
- inside
- surface_material
- surface_process
- emboss
- special_print
- bottom .
- material
- kadomaru .
- notch .
