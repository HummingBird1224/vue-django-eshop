# コーディング規則

ver 1.0.0 

### 命名
```
キャメル -> HelloWorld
スネーク -> hello_world
ケバブ -> hello-world
```

- クラス名：キャメル
- メソッド名：スネーク
- 関数名：スネーク
- 変数名：スネーク
- url: ケバブ
- url name: スネーク

### Prefix
|Prefix|内容|例|
|---|:---|:---|
|is	| 期待する状態になっているか| isEnabled|
|can | 期待する処理ができるか |	canRemove|
|should | 命令を実行するべきか | shouldMigrate|
|need |	命令を実行する必要があるか | needFileCopy|
|has | 期待するデータやプロパティを持っているか| hasKeyword|


### インデント

Python
- **必ずスペースに**
- 基本的にはPEP-8に基づく
- 行80文字以上は仕方ない場合のみ
- クラス間は2行空ける
- メソッド間、関数間は1行空ける


HTML
- インデント -> 2スペース

