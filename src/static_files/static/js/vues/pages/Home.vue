<template>
  <div class="p-home">
    <div class="p-homeMain">
      <div class="p-homeMain-body">
        <div class="p-homeMain-message">
          <h2 class="g-title-secondary">
            オリジナルパッケージで<br>
            より強いブランドづくりへ
          </h2>
          <div class="p-homeMain-message-tags">
            <div class="p-homeMain-message-tags-tag">
              <img :src="staticUrl + 'img/home/icimg_features03.png'" alt="">
              <p><b>最短30秒で<br />自動見積もり</b></p>
            </div>
            <div class="p-homeMain-message-tags-tag">
              <img :src="staticUrl + 'img/home/icimg_features05.png'" alt="">
              <p><b>平均コスト<br />20%ダウン</b></p>
            </div>
            <div class="p-homeMain-message-tags-tag">
              <img :src="staticUrl + 'img/home/icimg_features02.png'" alt="">
              <p><b>50枚から<br />発注可能</b></p>
            </div>
            <div class="p-homeMain-message-tags-tag">
              <img :src="staticUrl + 'img/home/icimg_features04.png'" alt="">
              <p><b>最短2週間で<br />納品</b></p>
            </div>
          </div>
          <div class="p-homeMain-smText">
            パッケージ発注の事前相談も可能です
          </div>
          <div class="p-homeMain-buttons">
            <a :href="'/catalog/flatbag'">
              <button class="c-btn c-btn--primary">
              パッケージを見る
              </button>
            </a>
            <a class="p-homeMain-buttons-contact" href="https://docs.google.com/forms/d/1YO31XLGTYHRW7E8Bpe8pZmDCeUudCvf0oMuPFNTvVLk/viewform" target="_blank">
              <button class="c-btn">
              お問い合わせはこちら
              </button>
            </a>
          </div>
        </div>
      </div>
      <div class="p-homeMain-smimg">
        <img :src="staticUrl + 'img/home/sp_package_bg.png'" alt="">
      </div>
      <div class="p-homeMain-left">
        <img :src="staticUrl + 'img/home/img_top_left.png'" alt="">
      </div>
      <div class="p-homeMain-right">
        <img :src="staticUrl + 'img/home/img_top_right.png'" alt="">
      </div>
    </div>

    <div class="p-homePartners p-home-content">
      <ul>
        <li class="p-homePartners-partner">
          <img :src="staticUrl + 'img/partners/fujimi_logo.svg'" alt="">
        </li>
        <li class="p-homePartners-partner">
          <img :src="staticUrl + 'img/partners/bulkhomme_logo.svg'" alt="">
        </li>
        <li class="p-homePartners-partner">
          <img :src="staticUrl + 'img/partners/kurashirumealkit_logo.svg'" alt="">
        </li>
        <li class="p-homePartners-partner">
          <img :src="staticUrl + 'img/partners/outdoorvoices_logo.png'" alt="">
        </li>
      </ul>
    </div>

    <div class="p-homePackages-md">
      <div class="p-homePackages-md-message">
        <h2>
          canalなら様々なデザインの<br>
          オリジナルパッケージが<br>
          簡単に作れます
        </h2>
        <a href="/catalog/flatbag">
          <button class="c-btn c-btn--primary">
          　パッケージを作る
          </button>
        </a>
      </div>
      <ul>
        <li v-for="(_p, index) in packages" :key="index">
          <a :href="_p.href" v-on:mouseover="setIsHoverPackage(index, true)" v-on:mouseleave="setIsHoverPackage(index, false)">
            <img :src="staticUrl + _p.src" alt="">
            <span v-show="isHoverPackage[index]">{{_p.label}}<i class="fas fa-arrow-right"></i></span>
          </a>
        </li>
      </ul>
    </div>

    <div class="p-homePackages-sm-wrap">
      <div class="p-homePackages-sm">
        <ul>
          <li v-for="(_p, index) in packages.slice(0, 7)" :key="index">
            <a :href="_p.href" v-on:mouseover="setIsHoverPackage(index, true)" v-on:mouseleave="setIsHoverPackage(index, false)">
              <img :src="staticUrl + _p.src" alt="">
              <span v-show="isHoverPackage[index]">{{_p.label}}<i class="fas fa-arrow-right"></i></span>
            </a>
          </li>
        </ul>
        <div class="p-homePackages-sm-message">
          <h2>
            canalなら様々なデザインの<br>
            オリジナルパッケージが<br>
            簡単に作れます
          </h2>
          <a href="/catalog/flatbag" target="_blank">
            <button class="c-btn c-btn--primary">
            　パッケージを作る
            </button>
          </a>
        </div>
        <ul>
          <li v-for="(_p, index) in packages.slice(7, 14)" :key="index">
            <a :href="_p.href" v-on:mouseover="setIsHoverPackage(index+7, true)" v-on:mouseleave="setIsHoverPackage(index+7, false)">
              <img :src="staticUrl + _p.src" alt="">
              <span v-show="isHoverPackage[index+7]">{{_p.label}}<i class="fas fa-arrow-right"></i></span>
            </a>
          </li>
        </ul>
      </div>
    </div>

    <div class="p-homeCategory p-home-content">
      <div class="p-homeCategory-body">
        <div class="p-home-content-header">
          <div class="p-home-content-topic">
            <p>PACKAGE CATEGORY</p>
          </div>
          <h3 class="g-title-tertiary">作れるパッケージは無限大</h3>
          <span>気になるカテゴリからパッケージを選択して<br>
              まずは自動見積もりしましょう</span>
        </div>
        <div class="p-homeCategory-wrap">
          <div class="p-homeCategory-item">
            <a :href="'/catalog/cardboard'">
              <img :src="staticUrl + 'img/home/cat_cardboard.jpg'" alt="">
              <h3 class="g-title-tertiary">ダンボール</h3>
              <p>一覧へ<i class="fas fa-arrow-right"></i></p>
            </a>
          </div>
          <div class="p-homeCategory-item">
            <a :href="'/catalog/flatbag'">
              <img :src="staticUrl + 'img/home/cat_flatbag.jpg'" alt="">
              <h3 class="g-title-tertiary">平袋</h3>
              <p>一覧へ<i class="fas fa-arrow-right"></i></p>
            </a>
          </div>
          <div class="p-homeCategory-item">
            <a :href="'/catalog/paperbox'">
              <img :src="staticUrl + 'img/home/cat_paperbox.jpg'" alt="">
              <h3 class="g-title-tertiary">紙器</h3>
              <p>一覧へ<i class="fas fa-arrow-right"></i></p>
            </a>
          </div>
        </div>
      </div>
      <div class="p-homeCategory-left">
        <img :src="staticUrl + 'img/home/container_ship.png'" alt="">
      </div>
    </div>

    <!--
    <div class="p-homeInterview p-home-content">
      <div class="p-homeInterview-body">
        <div class="p-home-content-header">
          <div class="p-home-content-topic">
            <p>INTERVIEW</p>
          </div>
          <h3 class="g-title-tertiary">canalはブランドづくりをお手伝いします</h3>
        </div>
        <div class="p-homeInterview-wrap">
          <div class="p-homeInterview-item">
            <a :href="'/'">
              <img :src="staticUrl + 'img/home/dummyGray.png'" alt="">
              <div class="p-homeInterview-item-description">
                <h3 class="g-title-tertiary">Oh My Teeth</h3>
                <p>会社名xxxxx 白ダンボール</p>
              </div>
              <div class="p-homeInterview-item-rightArrow"><i class="fas fa-arrow-right"></i></div>
            </a>
          </div>
          <div class="p-homeInterview-item">
            <a :href="'/'">
              <img :src="staticUrl + 'img/home/dummyGray.png'" alt="">
              <div class="p-homeInterview-item-description">
                <h3 class="g-title-tertiary">Oh My Teeth</h3>
                <p>会社名xxxxx 白ダンボール</p>
              </div>
              <div class="p-homeInterview-item-rightArrow"><i class="fas fa-arrow-right"></i></div>
            </a>
          </div>
          <div class="p-homeInterview-item">
            <a :href="'/'">
              <img :src="staticUrl + 'img/home/dummyGray.png'" alt="">
              <div class="p-homeInterview-item-description">
                <h3 class="g-title-tertiary">Oh My Teeth</h3>
                <p>会社名xxxxx 白ダンボール</p>
              </div>
              <div class="p-homeInterview-item-rightArrow"><i class="fas fa-arrow-right"></i></div>
            </a>
          </div>
        </div>
      </div>
      <div class="p-homeInterview-right">
        <img :src="staticUrl + 'img/home/container_ship.png'" alt="">
      </div>
    </div>
    -->

    <div class="p-homeHowto p-home-content">
      <div class="p-home-content-header">
        <div class="p-home-content-topic">
          <p>How To Use</p>
        </div>
        <h3 class="g-title-tertiary">
          発注までの流れ
        </h3>
      </div>
      <div class="p-homeHowto-content">
        <div class="p-homeHowto-box">
          <div class="p-homeHowto-box-svgWrapper">
            <svg width="32" height="25" viewBox="0 0 32 25" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M10.1818 19.2727L2.54545 11.6364L0 14.1818L10.1818 24.3636L32 2.54545L29.4545 0L10.1818 19.2727Z" fill="#205EFB"/>
            </svg>
          </div>
          <img :src="staticUrl + 'img/home/howtouse01.jpg'" alt="">
          <div class="p-homeHowto-box-description">
            <h4 class="g-title-quaternary">1. 希望のパッケージを選択</h4>
            <p>「サイズ」と「注文数」を表から選んで詳細へ</p>
          </div>
        </div>
        <div class="p-homeHowto-box">
          <div class="p-homeHowto-box-svgWrapper">
            <svg width="42" height="40" viewBox="0 0 42 40" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M33.5922 19.94C32.9122 21.18 31.5922 22 30.0922 22H15.1922L12.9922 26H36.9922V30H12.9922C9.95219 30 8.03219 26.74 9.49219 24.06L12.1922 19.18L4.99219 4H0.992188V0H7.53219L9.41219 4H39.0122C40.5322 4 41.4922 5.64 40.7522 6.96L33.5922 19.94ZM35.6122 8H11.3122L16.0522 18H30.0922L35.6122 8ZM12.9922 32C10.7922 32 9.01219 33.8 9.01219 36C9.01219 38.2 10.7922 40 12.9922 40C15.1922 40 16.9922 38.2 16.9922 36C16.9922 33.8 15.1922 32 12.9922 32ZM29.0122 36C29.0122 33.8 30.7922 32 32.9922 32C35.1922 32 36.9922 33.8 36.9922 36C36.9922 38.2 35.1922 40 32.9922 40C30.7922 40 29.0122 38.2 29.0122 36Z" fill="#205EFB"/>
            </svg>
          </div>
          <img :src="staticUrl + 'img/home/howtouse02.jpg'" alt="">
          <div class="p-homeHowto-box-description">
            <h4 class="g-title-quaternary">2. カートに入れて購入へ</h4>
            <p>
              内容を確認してカートへ。アカウント登録、配送先<br />
              支払い情報を入力して購入します。
            </p>
          </div>
        </div>
        <div class="p-homeHowto-box">
          <div class="p-homeHowto-box-svgWrapper">
            <svg width="28" height="36" viewBox="0 0 28 36" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M28 4L28 32C28 34.2 26.2 36 24 36L4 36C1.8 36 -1.49493e-06 34.2 -1.39876e-06 32L-1.74846e-07 4C-7.86805e-08 1.8 1.8 -1.14524e-06 4 -1.04907e-06L24 -1.74846e-07C26.2 -7.86805e-08 28 1.8 28 4ZM4 4L4 32L24 32L24 4L4 4Z" fill="#205EFB"/>
            </svg>
          </div>
          <img :src="staticUrl + 'img/home/howtouse03.jpg'" alt="">
          <div class="p-homeHowto-box-description">
            <h4 class="g-title-quaternary">3. 印刷デザインデータを作成・入稿</h4>
            <p>テンプレートをダウンロード。データを作成、入稿します。</p>
            <a href="https://same-raft-469.notion.site/canal-50e2a7a156fc4ae498e277996313e977"><p>データ作成に関してはこちらをご覧ください。</p></a>
          </div>
        </div>
        <div class="p-homeHowto-box">
          <div class="p-homeHowto-box-svgWrapper">
            <svg width="48" height="48" viewBox="0 0 48 48" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path fill-rule="evenodd" clip-rule="evenodd" d="M40 16H34V8H6C3.8 8 2 9.8 2 12V34H6C6 37.32 8.68 40 12 40C15.32 40 18 37.32 18 34H30C30 37.32 32.68 40 36 40C39.32 40 42 37.32 42 34H46V24L40 16ZM39 19L42.92 24H34V19H39ZM10 34C10 35.1 10.9 36 12 36C13.1 36 14 35.1 14 34C14 32.9 13.1 32 12 32C10.9 32 10 32.9 10 34ZM16.44 30C15.34 28.78 13.78 28 12 28C10.22 28 8.66 28.78 7.56 30H6V12H30V30H16.44ZM34 34C34 35.1 34.9 36 36 36C37.1 36 38 35.1 38 34C38 32.9 37.1 32 36 32C34.9 32 34 32.9 34 34Z" fill="#205EFB"/>
            </svg>
          </div>
          <img :src="staticUrl + 'img/home/howtouse04.jpg'" alt="">
          <div class="p-homeHowto-box-description">
            <h4 class="g-title-quaternary">4. 注文したパッケージが届きます</h4>
            <p>
              無事入稿したら注文完了です。お届けまでお待ちください。<br />
              「注文一覧」から配送状況を確認することも可能です。
            </p>
          </div>
        </div>
      </div>
    </div>

    <div class="p-homeGuide  p-home-content">
      <div class="p-home-content-header">
        <div class="p-home-content-topic">
          <p>お困りの際は</p>
        </div>
        <h3 class="g-title-tertiary">
          お問い合わせ/ご利用ガイド
        </h3>
      </div>
      <div class="p-homeGuide-content">
        <div class="p-homeGuide-item">
          <img :src="staticUrl + 'img/home/ic_contact.png'" alt="">
          <h3 class="g-title-tertiary">お求めの商品が見当たらない場合</h3>
          <p>
            パッケージや仕様に関してのご相談は<br>
            お気軽にご連絡ください。
          </p>
          <button class="c-btn"><a href="https://docs.google.com/forms/d/1YO31XLGTYHRW7E8Bpe8pZmDCeUudCvf0oMuPFNTvVLk/viewform" class="c-textLink" target="_blank">お問い合わせはこちらから</a></button>
        </div>
        <div class="p-homeGuide-item">
          <img :src="staticUrl + 'img/home/ic_contact-1.png'" alt="">
          <h3 class="g-title-tertiary">ご利用ガイド</h3>
          <p>
            データの作成方法、印刷で利用可能な色についてなど<br>
            ご不明なことがあればご覧ください。
          </p>
          <button class="c-btn"><a href="https://same-raft-469.notion.site/canal-50e2a7a156fc4ae498e277996313e977" class="c-textLink" target="_blank">ご利用ガイドへ</a></button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import StoreMixin from '../mixins/StoreMixin'

export default {
  name: 'Home',
  mixins: [StoreMixin],
  data: () => ({
    isHoverPackage: {},
    packages: [
      {label: 'ポスト投函用N式クラフト',
       src: 'img/home/packages/1.jpg',
       href: '/catalog/cardboard/ntype-mailer-craft/'},
      {label: '小分け袋',
       src: 'img/home/packages/2.jpg',
       href: '/catalog/flatbag/subsection-bag/'},
      {label: 'ジップ付き透明袋',
       src: 'img/home/packages/3.jpg',
       href: '/catalog/flatbag/zip-clear-pressbag/'},
      {label: 'ジップ付きアルミスタンド袋',
       src: 'img/home/packages/4.jpg',
       href: '/catalog/flatbag/zip-aluminum-stand-small-lot/'},
      {label: '宅配用N式クラフト',
       src: 'img/home/packages/5.jpg',
       href: '/catalog/cardboard/ntype-corrugated-craft/'},
      {label: 'B式組み立て底',
       src: 'img/home/packages/6.jpg',
       href: '/catalog/paperbox/folding-carton/'},
      {label: 'ジップ付きアルミスタンド袋',
       src: 'img/home/packages/7.jpg',
       href: '/catalog/flatbag/zip-aluminum-stand-small-lot/'},
      {label: '宅配用N式フルカラー',
       src: 'img/home/packages/8.jpg',
       href: '/catalog/cardboard/ntype-corrugated-white/'},
      {label: 'テープ付き不透明袋',
       src: 'img/home/packages/9.jpg',
       href: '/catalog/flatbag/tape-bag-small-lot/'},
      {label: 'テープ付き不透明袋',
       src: 'img/home/packages/10.jpg',
       href: '/catalog/flatbag/tape-bag-small-lot/'},
      {label: '宅配用A式クラフト',
       src: 'img/home/packages/11.jpg',
       href: '/catalog/cardboard/atype-craft/'},
      {label: '宅配用A式クラフト',
       src: 'img/home/packages/12.jpg',
       href: '/catalog/cardboard/atype-craft/'},
      {label: '宅配用A式クラフト',
       src: 'img/home/packages/13.jpg',
       href: '/catalog/cardboard/atype-craft/'},
      {label: 'テープ付き不透明袋',
       src: 'img/home/packages/14.jpg',
       href: '/catalog/flatbag/tape-bag-small-lot/'},
      {label: '宅配用N式フルカラー',
       src: 'img/home/packages/15.jpg',
       href: '/catalog/cardboard/ntype-corrugated-white/'},
      {label: 'ボックスパウチ',
       src: 'img/home/packages/16.jpg',
       href: '/catalog/flatbag/aluminum-pouche/'},
      {label: 'ポスト投函用たとう式クラフト',
       src: 'img/home/packages/17.jpg',
       href: '/catalog/cardboard/ttype-craft/'},
    ]
  }),
  components: {},
  computed: {
    staticUrl() {
      return this.state.staticUrl;
    }
  },
  methods: {
    setIsHoverPackage(index, isHover) {
      this.isHoverPackage[index] = isHover
    }
  },
  mounted() {
  }
}
</script>

<style scoped>
</style>
