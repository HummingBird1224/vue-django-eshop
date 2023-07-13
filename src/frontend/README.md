# CSSガイドライン

作業ディレクトリ: `src/static_files/static/css`

デフォルトで、 [sanitize.css](http://jonathantneal.github.io/sanitize.css/) がimportされていますが、用途に合わせてreset.cssに変えるなりしても良いと思います。（どのreset.cssを使うかというルール決めをするのも良いかもしれません）
CSSライブラリですが、 `yarn` で追加したものをimportするのがcleanで良いかと思われます.

## スタイルガイド

`/markup/parts-list`のURLにアクセスすると、使用頻度の高いCSSコンポーネントの使用例を見ることができます。


## CSSのディレクトリ構成

CSSのディレクトリ構成は、`style.scss`をCSSファイルの起点として、同じ階層に以下のディレクトリを作成し**この並び順に読み込まれる（カスケードする）ようにします**。

1. base （基礎）
2. components （部品）
3. pages （装飾）
4. vendor （ライブラリ等）

### CSSの構成例

以下の構成例を参考に新しいスタイル定義を追加してください。

```
※各ファイル名は参考例のため、実際には異なる場合や存在しない場合があります
src/static_files/static/
└── css/
     ├── style.scss           - CSSファイルの起点（エントリーポイント）
     ├── ...
     ├── base/                - 全体で使用する変数・関数・mixin等の定義
     │   ├── _variable.scss　 - 変数定義
     │   ├── _font.scss     　- フォントファミリーや、フォント関連の関数の定義
     │   ├── _mixin.scss    　- 全体で使用するminxin
     │   ├── _function.scss 　- 全体で使用するfunction
     │   ├── _utility.scss  　- utilityの定義
     │   └── _base.scss     　- html, body, aなどプリミティブなタグにおいての基本的なstyle定義
     ├── components/          - コンポーネント単位のスタイル定義
     │   ├── _btn.scss              - Buttonコンポーネント
     │   ├── _page.scss             - Pageコンポーネント
     │   └── ...
     ├── page/                - ページ単位のスタイル定義
     │   ├── _top.scss            - トップページ
     │   ├── _mypage.scss         - マイページ
     │   └── ...
     └─ vendor/              　- cssライブラリやプラグインのcssなど
```


## コーディングルール

### 分類用プレフィックス

baseを除き、グローバルCSSのディレクトリ構成に合わせて、そのディレクトリ名の「頭文字1文字+ハイフン」（componentsであれば`c-`）をプレフィックスとして使用します。
基本的にページ固有に定義するCSSセレクタ名、Sass変数名等にはこの分類用プレフィックスを付加しますが、何らかの理由でプレフィックスの付加が困難だったり、好ましくない場合は付けなくても構いません。

1. components （部品）
    * e.g. `.c-btn`, `.c-btn-text` (SUIT CSSの命名規則)
2. page （装飾）
    * e.g. `.p-mypage`, `.p-mypage-show` (SUIT CSSの命名規則)


### コンポーネントの命名規則(SUIT CSS)

このWORKSでは、**プロジェクト固有のコンポーネント**（前述のcomponentsとdecorationsディレクトリに含まれるSCSSファイル）の命名規則に[SUIT CSS](https://github.com/suitcss/suit/blob/master/doc/naming-conventions.md)を採用しています。「プロジェクト固有」にはCSSフレームワークやプラグインなどの**外部ライブラリは含まれません**。

SUIT CSSの命名規則は、[BEM](https://csswizardry.com/2013/01/mindbemding-getting-your-head-round-bem-syntax/)によく似た概念および命名で、重要なのは以下の5つのルールです。

1. **Component** （BEMのBlock相当）は、キャメルケースでComponent名を書く
    * 例：`.p-componentName`
2. **Descendent** （BEMのElement相当）は、Component名に続けてハイフン**1個**と頭文字**小文字**のキャメルケースでDescendent名を書きます。**必ずComponentの子要素**として配置します
    * 例：`.p-componentName-descendentName`
3. **Modifier** （BEMのModifier相当）は、ComponentのModifierとDescendentのModifierの2種類があります
    * **ComponentのModifier**: Component名に続けてハイフン**2個**と頭文字**小文字**のキャメルケースでModifier名を書きます。これをHTML上で使用する際は、**必ず元のComponentと連結**してクラス指定します
        * 例：`.p-componentName--modifierName`
    * **DescendentのModifier**: Descendent名に続けてハイフン**2個**と頭文字**小文字**のキャメルケースでModifier名を書きます。これをHTML上で使用する際は、**必ず元のComponentと連結**してクラス指定します
        * 例：`.p-componentName-descendentName--modifierName` (DescendentのModifier)
4. **ステート（状態を表す）クラス**は、`is-`プレフィックスを付けて頭文字**小文字**のキャメルケースで書き、**必ずComponent/Modifier/Descendentのどれかと連結**します
    * 例：`.p-componentName.is-stateName`, `.p-componentName-descendentName.is-stateName`, `.p-componentName--modifierName.is-stateName`

#### モディファイアとステートの違い

* モディファイア： **静的**に適用されるバリエーションを表現するために使用します。JSからは**操作しません**
    * 例えば、同じコンポーネントだけど使う場所によって背景色が違う、とか、マージンが違う、のようなケース
* ステート： **動的**に適用される状態を表現するために使用します。JSからも**操作します**
    * 例えば、その使用しているコンポーネント自体でON/OFFの状態がある、のようなケース

#### コンポーネント、モディファイアの使用例
* 初めは全てpageとして作成します。 例：`.p-brand-detail`
* 他のページで同じパーツが出てきた場合に、新しくscssファイルを作成し、componentとして抽出します。
例：`.p-brand-detail→.c-brandDetailに変更（_brandDetail.scss）`
* コンポーネントが、特定のページ内でのみ他の見た目になる場合は、モディファイアを使用します。モディファイアは、上書きされる要素側のscssファイル（ `_brandDetail.scss` ）に全て表記します。
 例：`c-brandDetail--cart`

```
HTMLではこのようクラスを指定します
<div class="c-brandDetail c-brandDetail--cart">
```
```
_brandDetail.scssのモディファイア例
/**************************
 * modifiers
 **************************/
$_: &;

// カート
&--cart {
  padding: 24px 0;

  @include mq() {
    width: 100%;
    padding: 0;
  }

  #{$_} {
    &-costText {
      width: 20%;
      min-width: 66px;
    }

    &-item {
      text-align: left;
    }

    &-add {
      display: block;
      text-align: left;
    }
  }
}
```

* 上書き箇所が少なければ、モディファイアとせずに、このような記載も可能です。
例： p-cartページ内で`c-brandDetail`を使用する場合。`c-brandDetail` と同じタグに、  `.p-cart-brandDetail` に追加分のレイアウト用のp-cart用のクラス名を付与する。 `_cart.scss` で上書きするクラスを記載します。

```
<div class="c-brandDetail p-cart-brandDetail">
```

### JavaScriptから参照・操作するセレクタの命名規則

JavaScriptから扱うセレクタには、`js-` または `is-` プレフィックスを付与し、それ以外の**CSS側で使われているセレクタを直接使用しない**ようにします。

* JavaScriptからのみ使用するid/class属性名のプレフィックスとして`js-`を付ける
    * 例） `#js-foo-list`、`.js-foo-list-item`
    * `js-`プレフィックスの付いたid/classには**CSSのスタイルを適用しない**
* JavaScriptから使用し、且つCSSのスタイルも適用するclass属性名のプレフィックスとして`is-`を付ける
    * 例） `.is-active`、`.is-hidden`
    * `is-`プレフィックスの付いたclassにはCSSのスタイルを適用してもよい（SUIT CSSの「状態を表すクラス」に該当）

``` haml
-# HTML例
<ul class="c-fooList" id="js-foo-list">
  <li class="f-fooList-item.js-foo-list-item">アイテムA</li>
  <li class="c-fooList-item.js-foo-list-item">アイテムB</li>
  <li class="c-fooList-item.js-foo-list-item is-hidden">アイテムC</li>
</ul>
```
``` scss
// CSS例
.c-fooList-item           { background-color: white; }
.c-fooList-item.is-active { background-color: yellow; }
.c-fooList-item.is-hidden { display: nonef }
```
``` coffeescript
# JavaScript例
if $('#js-foo-list').length > 0
  $('.js-foo-list-item').on 'click', ->
    $(this).addClass('is-active')
```
