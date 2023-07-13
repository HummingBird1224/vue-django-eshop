import json

data = {
    'contact_required': {
        'name': 'お問い合わせ',
        'value': False,
        "extra": "https://docs.google.com/forms/d/1YO31XLGTYHRW7E8Bpe8pZmDCeUudCvf0oMuPFNTvVLk/viewform",
        'image': '',
    },
    'sample_order': {
        'name': 'サンプル注文',
        'value': False,
        "extra": "https://docs.google.com/forms/d/1YO31XLGTYHRW7E8Bpe8pZmDCeUudCvf0oMuPFNTvVLk/viewform",
        'image': '',
    },
    'small_lot_availability': {
        'name': '小ロット対応',
        'value': False,
        'extra': '',
        'image': '',
    },
    'min_ordering_quantity': {
        'name': '最小注文数',
        'value': 50,
        'extra': '',
        'image': '',
    },
    'max_ordering_quantity': {
        'name': '最大注文数',
        'value': 300,
        'extra': '',
        'image': '',
    },
    'estimated_shipping_date': {
        'name': '納期',
        'value': {
            'first': 5,
            'repeat': 5
        },
        'extra': {
            'first': '3-5営業日',
            'repeat': '',
        },
        'image': '',
    },
    'can_select_original_size': {
        'name': 'オリジナルサイズ',
        'value': False,
        'extra': '',
        'image': '',
    },
    'is_design_unnecessary': {
        'name': 'デザイン不要',
        'value': True,
        'extra': '',
        'image': '',
    },
    'is_easy_draft_available': {
        'name': 'カンタン入稿可能',
        'value': False,
    },
    'notes': {
        'name': '備考',
        'value': '',
        'extra': [
            {'key': '厚み', 'value': '100サイズ横長以外は3mm、100サイズ横長は5mmです。'},
            {'key': 'サイズ', 'value': '外寸表記です。'},
            {'key': '①横', 'value': '外寸より6mm小さい(100サイズ横長は10mm)'},
            {'key': '②縦', 'value': '外寸より6mm小さい(100サイズ横長は10mm)'},
            {'key': '③高さ', 'value': '外寸より10mm小さい(100サイズ横長は15mm)'},
        ],
        'image': '',
    },
    'choosable_color': {
        'name': '印刷色',
        'value': "印刷はできません",
        'extra': '',
        'image': '',
    },
    'example': {
        'value': 27,
        'suffix': '円〜',
        'unit': '箱'
    },
    'size_limit': {
        'height': {
            'min': 100,
            'max': 550,
        },
        'width': {
            'min': 250,
            'max': 610,
        },
        'depth': {
            'min': 135,
            'max': 550,
        },
    },
    'shipping_area': {
        'exclude': False,
        'prefectures': [
            '東京',
            '神奈川',
            '静岡',
            '埼玉',
            '千葉',
        ]
    },
    'required_fields': {
        'size': [
            "height",
            "depth",
            "width",
        ],
        "color_num": None,
        "quantity": None,
    },
    'option_order': [
        'color_num',
        'size',
        'quantity'
    ],
    'quantity': {
        'name': '注文数',
        'extra': '',
        'required': True,
        'default': '5',
        'image': '',
        'unit': '箱',
        'widget_type': 'radio',
        'options': {
            '5': {'name': '50', 'value': 50},
            '10': {'name': '100', 'value': 100},
            '15': {'name': '150', 'value': 150},
            '20': {'name': '200', 'value': 200},
            '30': {'name': '300', 'value': 300},
        },
    },
    'size': {
        'name': 'サイズ',
        'extra': 'サイズを選択してください',
        'required': True,
        'default': '1',
        'image': '',
        'widget_type': 'modal-radio',
        'options': {
            '1': {
                'name': '60サイズ',
                'value': [
                    {'name': 'height', 'value': 120},
                    {'name': 'width', 'value': 250},
                    {'name': 'depth', 'value': 210},
                ],
                'extra': '高さ120mm 幅250mm 奥行き210mm',
                'image': 'img/product_detail/cardboard/size/atype-plain/60.jpg',
                'data': ''
            },
            '2': {
                'name': '80サイズ正方形',
                'value': [
                    {'name': 'height', 'value': 190},
                    {'name': 'width', 'value': 250},
                    {'name': 'depth', 'value': 190},
                ],
                'extra': '高さ190mm 幅250mm 奥行き190mm',
                'image': 'img/product_detail/cardboard/size/atype-plain/80_square.jpg',
                'data': ''
            },
            '3': {
                'name': '80サイズ',
                'value': [
                    {'name': 'height', 'value': 150},
                    {'name': 'width', 'value': 310},
                    {'name': 'depth', 'value': 220},
                ],
                'extra': '高さ150mm 幅310mm 奥行き220mm',
                'image': 'img/product_detail/cardboard/size/atype-plain/80.jpg',
                'data': ''
            },
            '4': {
                'name': '80サイズ横長',
                'value': [
                    {'name': 'height', 'value': 100},
                    {'name': 'width', 'value': 400},
                    {'name': 'depth', 'value': 200},
                ],
                'extra': '高さ100mm 幅400mm 奥行き200mm',
                'image': 'img/product_detail/cardboard/size/atype-plain/80_wide.jpg',
                'data': ''
            },
            '5': {
                'name': '100サイズ',
                'value': [
                    {'name': 'height', 'value': 250},
                    {'name': 'width', 'value': 350},
                    {'name': 'depth', 'value': 300},
                ],
                'extra': '高さ250mm 幅350mm 奥行き300mm',
                'image': 'img/product_detail/cardboard/size/atype-plain/100.jpg',
                'data': ''
            },
            '6': {
                'name': '100サイズ横長',
                'value': [
                    {'name': 'height', 'value': 230},
                    {'name': 'width', 'value': 435},
                    {'name': 'depth', 'value': 310},
                ],
                'extra': '高さ230mm 幅435mm 奥行き310mm',
                'image': 'img/product_detail/cardboard/size/atype-plain/100_wide.jpg',
                'data': ''
            },
            '7': {
                'name': '120サイズ',
                'value': [
                    {'name': 'height', 'value': 275},
                    {'name': 'width', 'value': 470},
                    {'name': 'depth', 'value': 330},
                ],
                'extra': '高さ230mm 幅435mm 奥行き310mm',
                'image': 'img/product_detail/cardboard/size/atype-plain/120.jpg',
                'data': ''
            },
        },
    },
    'color_num': {
        'name': '印刷に使用する色数',
        'extra': '',
        'required': True,
        'default': '1',
        'image': '',
        'widget_type': 'slider-sm',
        'options': {
            '1': {
                'name': '無地',
                'value': 0,
                'extra': '素材そのままの無地状態です。',
                'image': 'img/product_detail/common/color_num/color_num_01.png'
            },
        },
        'note': {
            "title": "印刷と色について",
            "sections": [
                {
                    "title": "印刷と料金について",
                    "layout_type": "horizontal-list-sm",
                    "summary": {
                        "title": "印刷に使用する色数で料金が変化します",
                        "body": [
                            '印刷に利用する色は<span class="js-external-link" data-link="https://same-raft-469.notion.site/8ac79f8c2b1744409560b4000586fd88">『ご利用ガイド：印刷色の選び方』</span>をご覧ください',
                        ]
                    },
                    "contents": [
                        {
                            'title': '１色',
                            'image': 'img/product_detail/common/color_num/color_num_01.png',
                        },
                        {
                            'title': '２色',
                            'image': 'img/product_detail/common/color_num/color_num_02.png'
                        },
                        {
                            'title': '３色',
                            'image': 'img/product_detail/common/color_num/color_num_03.png'
                        },
                        {
                            'title': '４色',
                            'image': 'img/product_detail/common/color_num/color_num_04.png'
                        }
                    ]
                },
                {
                    "title": "使用可能な色数が生地で変わります",
                    "layout_type": "vertical-list-md",
                    "contents": [
                        {
                            "title": "使用可能が色があります",
                            "image": "img/product_detail/cardboard/color_limitation/cardbox_materialcolor_limit.jpg",
                            "body": [
                                '<span class="js-open-color-list-modal-btn">こちらから利用可能な色を確認できます。</span>',
                            ]
                        },
                        {
                            "title": "どんな色でもOK",
                            "image": "img/product_detail/cardboard/color_limitation/cardbox_materialcolor_free.jpg",
                            "body": [
                                "合紙ならどんな色でも印刷可能です。",
                            ]
                        }
                    ]
                },
            ]
        }
    },
}


print(json.dumps(data, indent=2, ensure_ascii=False))
