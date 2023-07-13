const imgBasePath = "img/explain_modal/";

const cardBoardColorExplain = {
  title: "ダンボール : 印刷の色",
  description: [
    `納期は購入後、データの入稿が確定した時点で決定します。
    データ入稿までの流れは以下です。`,
    // {
    //   headline: "1.小ロットの場合",
    //   description:
    //     "小ロット（注文数〜500）で注文をする場合は印刷に使用できる色が、「白」「黒」「赤」「青」「緑」に限られます。具体的な色は画像を参照下さい。",
    // },
    // { src: imgBasePath + "cardboard_small_lot_color_sample.png" },
    {
      headline: "1.クラフト/ホワイト生地の場合",
      description:
        "フレキソ印刷の場合、印刷の中でもともと使うインクが用意されていて、その中から選ぶ仕組み。そこにない色を作ることもできますが、ゼロからインクを作るため費用がかかるためお問い合わせください。",
    },
    { src: imgBasePath +  "cardboard_normalcolor_sample.png" },
    { src: imgBasePath + "cardboard_whitecolor_sample.png" },
    {
      headline: "2.合紙の場合",
      description: `CMYKで作成されたどの色でも印刷することが可能です。
      印刷データをCMYKモードにして作成してください。`,
    },
  ],
};

const flatBagColorExplain = {
  title: "平袋 : 印刷の色",
  description: [
    "平袋では印刷に使う色はPANTONEから選ぶ必要があります。",
    {
      headline: "1.PANTONEのサイトから色を選択",
      description: `PANTONEのサイトから色を選びください。
        PANTONEから色を選ぶ際には「◯◯◯ C」または「◯◯◯ U」という名前（〇〇〇には数字3桁が入ります）の色をお選びください。ハイフンなどがついているものは色味の再現のために色見本を送って頂く必要があります。`,
    },
    "▼ PANTONEカラーの一覧",
    {
      link:
        "https://www.pantone.jp/color-finder#/pick?pantoneBook=pantoneSolidCoated",
    },
    { src: imgBasePath + "flatbag_pantone_sample.png" },
    {
      headline: "2. 黒色または白色の場合",
      description:
        `PANTONEの中に該当する色がないので
        ・デザインツールで黒or白を表現してデータを作成していただいて構いません
        ・作成するデータに”「黒色/白色」を使う”という表記を追加してください。`,
    },
  ],
};

const cardBoardDraftExplain = {
  title: "データ入稿方法について",
  description: [
    `オリジナルパッケージの発注は購入だけでは完了しません、データの作成が必要です。
    2種類のデータ作成方法から選択できます。`,
    { src: imgBasePath + "cardboard_draft_methods.png" },
    {
      headline: "1. カンタン入稿",
      description: `一部のダンボールパッケージが対応している入稿方法です。
        【対応パッケージ】
        印刷デザイン数:1つ、印刷面数:1~2つの時のみ利用できます。
        ・配送箱(A式/みかん箱)
        ・配送箱N式
        ・梱包箱N式
        ・ポスト投函箱（たとう式)`,
    },
    {
      headline: "2. データを作成して入稿",
      description: `ご自身で入稿データを作成する方法です。
      canal上で選択できるパッケージのサイズに関してはテンプレートをダウンロードして利用できます。`,
    },
    { link: "https://same-raft-469.notion.site/39dcfa24bb2b437393041b98f2b1d657", text: "▶︎データ作成の注意事項はコチラ"},
    { link: "https://same-raft-469.notion.site/e3c4cc81f12247d694408fd9b59a6b7a", text: "▶︎テンプレート一覧はコチラ" },
  ],
};

const flatBagDraftExplain = {
  title: "データ入稿方法について",
  description: [
    `オリジナルパッケージの発注は購入だけでは完了しません、データの作成が必要です。
    2種類のデータ作成方法から選択できます。`,
    { src: imgBasePath + "flatbag_draft_methods.png" },
    {
      headline: "1. カンタン入稿",
      description: `画像データをアップロードするだけで入稿データを作成する方法です。`,
    },
    {
      headline: "2. データを作成して入稿",
      description: `ご自身で入稿データを作成する方法です。
      canal上で選択できるパッケージのサイズに関してはテンプレートをダウンロードして利用できます。`,
    },
    { link: "https://same-raft-469.notion.site/39dcfa24bb2b437393041b98f2b1d657", text: "▶︎データ作成の注意事項はコチラ"},
    { link: "https://same-raft-469.notion.site/e3c4cc81f12247d694408fd9b59a6b7a", text: "▶︎テンプレート一覧はコチラ" },
  ],

};

const flatBagPlateChargeExplain = {
  title: "版代 / 木型代とは",
  description: [
    `オリジナル印刷を施すのに必要な初期費用です。
    入稿データにつき、印刷用の版(板)を作ります。
    1色につき1版必要になるので、デザインに使用する色の数だけ版代がかかります。`,
    { src: imgBasePath + "version_charge_description.png" },
    {
      headline: "①初期費用として初回の発注の時のみ発生します",
      description: `基本的には初回のみ費用が発生します。
      再発注する場合は同サイズのパッケージを再発注すれば版代は必要ありません。
      ただし、「再発注でパッケージサイズを変更」、「ロット数の一部変更」の場合は
      再発注だとしても版代が発生してしまいます。`,
    },
    {
      headline: "②同サイズのパッケージなら2回目以降、版代は発生しません",
      description: "納期は購入後、データの入稿が確定した時点で決定します。",
    },
    {
      headline: "③ロット数の範囲が変わると、版代が発生することがあります",
      description: `小ロットと大ロットの範囲を変更して再発注すると、版代が発生します。
      ○小ロット : 10~3000
      ○大ロット : 3000~`,
    },
    {
      headline: "④最終注文から1.5~2年経つともう1度費用が発生します",
      description:
        "最後の注文から時間が経過した場合、再び版代/木型代が発生する場合がございます。",
    },
  ],
};

const cardboardPlateChargeExplain = {
  title: "版代 / 木型代とは",
  description: [
    `オリジナル印刷を施すのに必要な初期費用です。
    入稿データにつき、印刷用の版(板)を作ります。
    1色につき1版必要になるので、デザインに使用する色の数だけ版代がかかります。`,
    { src: imgBasePath + "version_charge_description.png" },
    {
      headline: "①初期費用として初回の発注の時のみ発生します",
      description: `基本的には初回のみ費用が発生します。
      再発注する場合は同サイズのパッケージを再発注すれば版代は必要ありません。
      ただし、「再発注でパッケージサイズを変更」、「ロット数の一部変更」の場合は
      再発注だとしても版代が発生してしまいます。`,
    },
    {
      headline: "②同サイズのパッケージなら2回目以降、版代は発生しません",
      description: "納期は購入後、データの入稿が確定した時点で決定します。",
    },
    {
      headline: "③ロット数の範囲が変わると、版代が発生することがあります",
      description: `小ロットと大ロットの範囲を変更して再発注すると、版代が発生します。
      ○小ロット : 50~300
      ○大ロット : 300~`,
    },
    {
      headline: "④最終注文から1.5~2年経つともう1度費用が発生します",
      description:
        "最後の注文から時間が経過した場合、再び版代/木型代が発生する場合がございます。",
    },
  ],
};

const paperboxPlateChargeExplain = {
  title: "版代 / 木型代とは",
  description: [
    `オリジナル印刷を施すのに必要な初期費用です。
    入稿データにつき、印刷用の版(板)を作ります。
    1色につき1版必要になるので、デザインに使用する色の数だけ版代がかかります。`,
    { src: imgBasePath + "version_charge_description.png" },
    {
      headline: "①初期費用として初回の発注の時のみ発生します",
      description: `基本的には初回のみ費用が発生します。
      再発注する場合は同サイズのパッケージを再発注すれば版代は必要ありません。
      ただし、「再発注でパッケージサイズを変更」、「ロット数の一部変更」の場合は
      再発注だとしても版代が発生してしまいます。`,
    },
    {
      headline: "②同サイズのパッケージなら2回目以降、版代は発生しません",
      description: "納期は購入後、データの入稿が確定した時点で決定します。",
    },
    {
      headline: "③ロット数の範囲が変わると、版代が発生することがあります",
      description: `小ロットと大ロットの範囲を変更して再発注すると、版代が発生します。
      ○小ロット : 50~300
      ○大ロット : 300~`,
    },
    {
      headline: "④最終注文から1.5~2年経つともう1度費用が発生します",
      description:
        "最後の注文から時間が経過した場合、再び版代/木型代が発生する場合がございます。",
    },
  ],
};

const howToFixTotalPrice = {
  title: "料金が決まる仕組み",
  description: [
    `納期は購入後、データの入稿が確定した時点で決定します。
データ入稿までの流れは以下です。`,
    { src: imgBasePath + "total_price_decision_process.png" },
    {
      headline: "1. 商品代金",
      description: "パッケージそのものの代金です。",
    },
    {
      headline: "2. 版代・木型代",
      description: `オリジナル印刷を施すのに必要な初期費用です。
      入稿データにつき、印刷用の版(板)を作ります。
      1色につき1版必要になるので、デザインに使用する色の数だけ版代がかかります。`,
    },
    {
      headline: "3. 消費税",
      description:
        "商品・製品の販売やサービスの提供などの取引に対して掛かる税です。",
    },
    {
      headline: "4. 送料",
      description: "現在は無料です。",
    },
  ],
};

const howToFixDeliveryDate = {
  title: "納期が決まるまでの仕組み",
  description: [
    { src: imgBasePath + "delivery_date_decision_process.png" },
    {
      headline: "1. パッケージの種類によって納期は変わります",
      description: "納期の目安は商品によって異なります。それぞれの商品ページをご確認ください。",
    },
    {
      headline: "2. データを確定した後に決定します",
      description: "納期は購入後、データの入稿が確定した時点で決定します。",
    },

  ],
};

const priceAndDesignRelationExplain = {
  title: "面数と値段の仕組み",
  description: [
    `印刷する面数が増えると基本的に料金が増加します。
    印刷するのに必要な”版”が、面数が増えることによって増加して版代が増えることで料金が増加する仕組みです。`,
  ],
};

//---------- CardboardPrintArea
const printAreaCardboardtypeA = {
  title: "印刷可能範囲について",
  description: [
    "配送箱A式ダンボールの印刷範囲について。",
    {
      headline: "1.注文数が500未満の場合",
      description:
        "小ロット(注文数が500以下)の場合はサイズによって印刷可能範囲が変化します。",
    },
    {
      src: imgBasePath + "print_area_cardboard_typea_1.png",
    },
    {
      headline: "190x100mmの印刷範囲のサイズ",
      description: `・60サイズ(幅250×奥行き210×高さ120) ・60サイズ横長(幅250×奥行き190×高さ190)
      ・80サイズ(幅310×奥行き220×高さ150) ・100サイズ(幅350×奥行き300×高さ250)
      ・100サイズ横長(幅435×奥行き310×高さ230)`,
    },
    {
      headline: "190x80mmの印刷範囲のサイズ",
      description: "・80サイズ横長(幅400×奥行き200×高さ100)",
    },
    {
      headline: "2.注文数が500以上の場合",
    },
    {
      src: imgBasePath + "print_area_cardboard_typea_2.png",
    }
  ],
};

const printAreaCardboardtypeNKonpo = {
  title: "印刷可能範囲について",
  description: [
    "梱包箱N式ダンボールの印刷範囲について。",
    {
      headline: "1.注文数が500未満の場合",
      description:
        "小ロット(注文数が500以下)の場合はサイズによって印刷可能範囲が変化します。",
    },
    {
      src: imgBasePath + "print_area_cardboard_typen_konpo_1.png",
    },
    {
      headline: "190×100mmの印刷範囲のサイズ",
      description: `・A5サイズ(幅235×奥行き165×高さ45)
      ・B5サイズ(幅275×奥行き200×高さ60)
      ・B6横長サイズ(幅285×奥行き135×高さ70)
      ・A4サイズ(幅330×奥行き230×高さ40)`,
    },
    {
      headline: "170×100mmの印刷範囲のサイズ",
      description: "・B6サイズ(幅190×奥行き135×高さ35)",
    },
    {
      headline: "145×80mmの印刷範囲のサイズ",
      description: "・A6サイズ(幅165×奥行き100×高さ35)",
    },
    {
      headline: "130×100mmの印刷範囲のサイズ",
      description: "・正方形サイズ(幅150×奥行き150×高さ50)",
    },
    {
      headline: "2.注文数が500以上の場合",
    },
    {
      src: imgBasePath + "print_area_cardboard_typen_konpo_2.png",
    },
    {
      headline: "全面印刷、ベタ塗りしたい場合",
      description:
        "・データを作成する際に、面の罫線から外側に3mmほど塗り足してください。",
    },
    {
      headline: "フルカラー印刷",
      description: "・印刷の制限はありません。CMYKカラー。",
    },
  ],
};
const printAreaCardboardtypeNHaiso = {
  title: "印刷可能範囲について",
  description: [
    "配送箱N式ダンボールの印刷範囲について。",
    {
      headline: "1. 注文数が500未満の場合",
      description:
        "小ロット(注文数が500以下)の場合はサイズによって印刷可能範囲が変化します。",
    },
    {
      src: imgBasePath + "print_area_cardboard_typen_haiso_1.png",
    },
    {
      headline: "145×100mmの印刷範囲のサイズ",
      description: "・A6サイズ(幅165×奥行き120×高さ30)",
    },
    {
      headline: "175×100mmの印刷範囲のサイズ",
      description: "・B6サイズ(幅195×奥行き140×高さ30)",
    },
    {
      headline: "190×100mmの印刷範囲のサイズ",
      description: `・A5サイズ(幅220×奥行き160×高さ30)
・B5サイズ(幅275×奥行き200×高さ30)
・A4サイズ(幅310×奥行き225×高さ30)`,
    },
    {
      headline: "2. 注文数が500以上の場合",
    },
    {
      src: imgBasePath + "print_area_cardboard_typen_haiso_2.png",
    },
    {
      headline: "全面印刷、ベタ塗りしたい場合",
      description:
        "・データを作成する際に、面の罫線から外側に3mmほど塗り足してください。",
    },
    {
      headline: "フルカラー印刷",
      description: "・印刷の制限はありません。CMYKカラー。",
    },
  ],
};

const printAreaCardboardTatou = {
  title: "印刷可能範囲について",
  description: [
    "たとう式ダンボールの印刷範囲について。",
    {
      headline: "1. 注文数が500未満の場合",
    },
    {
      src: imgBasePath + "print_area_cardboard_tatou_1.png",
    },
    {
      headline: "190×100mmの印刷範囲のサイズ",
      description: `・A5サイズ(幅235×奥行き176×高さ25)
      ・A4小サイズ(幅310×奥行き228×高さ25)
      ・A4サイズ(幅335×奥行き248×高さ30)`,
    },
    {
      headline: "2. 注文数が500以上の場合",
    },
    {
      src: imgBasePath + "print_area_cardboard_tatou_2.png",
    },
    {
      headline: "全面印刷、ベタ塗りしたい場合",
      description:
        "・データを作成する際に、面の罫線から外側に3mmほど塗り足してください。",
    },
    {
      headline: "フルカラー印刷",
      description: "・印刷の制限はありません。CMYKカラー。",
    },
  ],
};

//---------- FlatBagPrintArea
const printAreaFlatbagTapedOPP = {
  title: "テープ付きOPP袋の印刷範囲について。",
  description: [
    {
      headline: "1. 注文数が3,000以下の場合",
    },
    {
      src: imgBasePath + "print_area_flatbag_opp_1.png",
    },
    {
      headline: "10x10cmの印刷範囲のサイズ",
      description: "・A6（110×155mm+30mm）",
    },
    {
      headline: "15x15cmの印刷範囲のサイズ",
      description: `・A5（160×220mm+30mm）
      ・A4（225×305mm+40mm）`,
    },
    {
      headline: "2. 注文数が3,000以上の場合",
    },
    {
      src: imgBasePath + "print_area_flatbag_opp_2.png",
    },
  ],
};

const printAreaFlatbagPressBag = {
  title: "印刷可能範囲について",
  description: [
    "以下の点に注意して印刷データを作成してください。",
    {
      headline: "面の端から数mmの余白を空けてデータを作成してください",
    },
    {
      src: imgBasePath + "print_area_flatbag_press_bag_1.png",
    },
    {
      headline: "全面印刷、ベタ塗りも可能です",
      description:
        "・データを作成する際に、面の罫線から外側に3mmほど塗り足してください。",
    },
  ],
};

const printAreaFlatbagTapeBag = {
  title: "テープ付き不透明袋の印刷範囲について。",
  description: [
    {
      headline: "1. 注文数が3,000以下の場合",
    },
    {
      src: imgBasePath + "print_area_flatbag_tapebag_1.png",
    },
    {
      headline: "200×290mmの印刷範囲のサイズ",
      description: "・A4 - 220mm×310mm+40mm",
    },
    {
      headline: "230×320の印刷範囲のサイズ",
      description: "・クリックポスト - 250mm×340mm+40mm",
    },
    {
      headline: "2. 注文数が3,000以上の場合",
      description: "・クリックポスト - 250mm×340mm+40mm",
    },
    {
      src: imgBasePath + "print_area_flatbag_tapebag_2.png",
    }
  ],
};

const printAreaFlatbagZipAlmi = {};

const printAreaFlatbagZipClear = {
  title: "印刷可能範囲について",
  description: [
    "ジップ付opp圧着なしの印刷範囲について。",
    {
      headline: "1. 注文数が3,000以下の場合",
    },
    {
      src: imgBasePath + "print_area_flatbag_zip_clear_1.png",
    },
    {
      headline: "10x10cmの印刷範囲のサイズ",
      description: `・小物用(100mm×140mm+チャック上20mm)
      ・A6(120mm×170mm+チャック上20mm)
      ・A5(170mm×240mm+チャック上20mm)
      ・A4(240mm×340mm+チャック上20mm)`,
    },
    {
      headline: "15x15cmの印刷範囲のサイズ",
      description: "・A3(340mm×480mm+チャック上20mm)",
    },
    {
      headline: "2. 注文数が3,000以上の場合",
    },
    {
      src: imgBasePath + "print_area_flatbag_zip_clear_2.png",
    },
  ],
};

const printAreaFlatbagAlmiClear = {
  title: "印刷可能範囲について",
  description: [
    "ジップ付き前透明アルミ袋の印刷範囲について",
    {
      headline: "1. 注文数が3,000以下の場合",
    },
    {
      src: imgBasePath + "print_area_flatbag_almi_clear_1.png",
    },
    {
      headline: "4x5cmの印刷範囲のサイズ",
      description: "・小物用(100×140mm+チャック上32mm)",
    },
    {
      headline: "5x5cmの印刷範囲のサイズ",
      description: "・A6(120×170mm+チャック上32mm)"
    },
    {
      headline: "8x10cmの印刷範囲のサイズ",
      description: "・B6(140×200mm+チャック上32mm)"
    },
    {
      headline: "10x10cmの印刷範囲のサイズ",
      description: "・A5(170×240mm+チャック上32mm)"
    },
    {
      headline: "2. 注文数が3,000以上の場合"
    },
    {
      src: imgBasePath + "print_area_flatbag_almi_clear_2.png",
    },
  ],
};

const printAreaFlatbagAlmiStand = {};

const printAreaFlatbagAlmi = {};

const printAreaFlatbagTaped = {};

const printAreaFoldingCarton = {
  title: "印刷可能範囲について",
  description: [
    "B式組み立て底の印刷範囲について",
    {
      headline: "キャラメル底の場合",
      description: "制限なく全面に印刷が可能です。",
    },
    {
      headline: "ワンタッチ底の場合",
      description: "底面を貼り合わせてかつ組み合わせる都合上、ロゴなどの印刷を位置を合わせることが難しく、底面は原則として全面ベタ印刷のみとなります。",
    },
  ],
};

const printAreaCushionEnvelope = {};

export {
  cardBoardColorExplain,
  cardBoardDraftExplain,
  flatBagColorExplain,
  flatBagDraftExplain,
  flatBagPlateChargeExplain,
  cardboardPlateChargeExplain,
  paperboxPlateChargeExplain,
  howToFixTotalPrice,
  howToFixDeliveryDate,
  priceAndDesignRelationExplain,
  printAreaCardboardtypeA,
  printAreaCardboardtypeNKonpo,
  printAreaCardboardtypeNHaiso,
  printAreaCardboardTatou,
  printAreaFlatbagTapedOPP,
  printAreaFlatbagZipAlmi,
  printAreaFlatbagZipClear,
  printAreaFlatbagAlmiStand,
  printAreaFlatbagAlmi,
  printAreaFlatbagAlmiClear,
  printAreaFlatbagTapeBag,
  printAreaFlatbagPressBag,
  printAreaFoldingCarton,
  printAreaCushionEnvelope,
};
