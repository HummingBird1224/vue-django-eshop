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
        'value': True,
        "extra": "https://docs.google.com/forms/d/1YO31XLGTYHRW7E8Bpe8pZmDCeUudCvf0oMuPFNTvVLk/viewform",
        'image': '',
    },
    'small_lot_availability': {
        'name': '小ロット対応',
        'value': True,
        'extra': '',
        'image': '',
    },
    'min_ordering_quantity': {
        'name': '最小注文数',
        'value': 100,
        'extra': '',
        'image': '',
    },
    'max_ordering_quantity': {
        'name': '最大注文数',
        'value': 3000,
        'extra': '',
        'image': '',
    },
    'estimated_shipping_date': {
        'name': '納期',
        'value': {
            'first': 14,
            'repeat': 7
        },
        'extra': {
            'first': 'データ確定後2週間',
            'repeat': '1週間',
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
        'value': False,
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
            {'key': '基材構成', 'value': 'OPP#40-50 (※袋のサイズによって変わります)'},
            {'key': 'フタの長さ', 'value': '30 ~ 40mm (※袋のサイズによって変わります)'},
        ],
        'image': '',
    },
    'print_area': {
        'name': '印刷可能範囲',
        'value': 5,
        'extra': '端から5mmの余白を開ける必要があり、その部分は印刷ができません。',
        'image': 'img/product_detail/film/print_area/5mm.jpg',
    },
    'example': {
        'name': 'Tシャツ梱包用',
        'price': '4.3円/袋',
        'quantity': '17,000袋印刷',
        'color_num': '1色印刷',
        'size': 'A4サイズ（160mm × 140mm + フタ40mm）',
        'image': 'img/product_detail/common/example/tape_opp_bag_example.jpg',
        'extras': [
            ''
        ]
    },
    'size_limit': {
        'height': {
            'min': 110,
            'max': 550,
        },
        'width': {
            'min': 80,
            'max': 400,
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
        'default': '1',
        'image': '',
        'unit': '袋',
        'widget_type': 'radio',
        'options': {
            '1': {'name': '100', 'value': 100},
            '2': {'name': '200', 'value': 200},
            '3': {'name': '300', 'value': 300},
            '5': {'name': '500', 'value': 500},
            '10': {'name': '1,000', 'value': 1000},
            '15': {'name': '1,500', 'value': 1500},
            '20': {'name': '2,000', 'value': 2000},
            '30': {'name': '3,000', 'value': 3000},
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
                'name': 'A6サイズ',
                'value': [
                    {'name': 'height', 'value': 155},
                    {'name': 'width', 'value': 110},
                    {'name': 'lip', 'value': 30},
                ],
                'extra': '高さ155mm 幅110mm',
                'image': 'img/external/futureshop/size/tape-opp-bag/a6.jpg',
                'data': ''
            },
            '2': {
                'name': ' A5サイズ',
                'value': [
                    {'name': 'height', 'value': 220},
                    {'name': 'width', 'value': 160},
                    {'name': 'lip', 'value': 30},
                ],
                'extra': '高さ220mm 幅160mm',
                'image': 'img/external/futureshop/size/tape-opp-bag/a5.jpg',
                'data': ''
            },
            '3': {
                'name': 'A4サイズ',
                'value': [
                    {'name': 'height', 'value': 305},
                    {'name': 'width', 'value': 225},
                    {'name': 'lip', 'value': 40},
                ],
                'extra': '高さ305mm 幅225mm',
                'image': 'img/external/futureshop/size/tape-opp-bag/a4.jpg',
                'data': ''
            },
        }
    },
    'color_num': {
        'name': '印刷カラー',
        'extra': '',
        'required': True,
        'default': '1',
        'image': '',
        'widget_type': 'slider-sm',
        'options': {
            '1': {
                'name': '１色',
                'value': 1,
                'extra': '印刷するデザインに使用する色数が１色の場合です。 生地や材質の色は含みません。',
                'image': 'img/product_detail/common/color_num/color_num_01.png'
            },
            '2': {
                'name': '２色',
                'value': 2,
                'extra': '印刷するデザインに使用する色数が２色の場合です。 生地や材質の色は含みません。',
                'image': 'img/product_detail/common/color_num/color_num_02.png'
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
                            '印刷に利用する色は<span class="js-external-link" data-link="https://same-raft-469.notion.site/acaa6c5ea5294bc6a74494970299305a">『PANTONEの見本からお選びください』</span>をご覧ください',
                            "色数が増えると基本的に料金が上がります",
                            "５色以上扱う場合、写真はフルカラーに該当します。"
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
                        },
                        {
                            'title': 'フルカラー',
                            'image': 'img/product_detail/common/color_num/color_num_full.png'
                        }
                    ]
                },
                {
                    "title": "印刷可能な範囲",
                    "layout_type": "vertical-list-lg",
                    "contents": [
                        {
                            "image": "img/product_detail/film/print_area/full.jpg",
                            "body": [
                                "端から5mmの余白を開ける必要があり、その部分は印刷ができません。",
                            ]
                        },
                    ]
                },
            ]
        }
    },
    'choosable_color': [
        {'name': '1色 - モノクロ', 'image': 'img/external/futureshop/color/monokuro.png'},
        {'name': '2色(PANTONEから選択)',
         'link': 'https://same-raft-469.notion.site/acaa6c5ea5294bc6a74494970299305a',
         'image': 'img/external/futureshop/color/pantone.png'},
    ],
}

print(json.dumps(data, indent=2, ensure_ascii=False))
