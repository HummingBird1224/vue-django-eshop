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
            {'key': 'ジップ上', 'value': '20mm'},
            {'key': '注文枚数で材質が少し変化します。', 'value': ''},
            {'key': '100-1000枚', 'value': 'IPP#60'},
            {'key': '', 'value': '→透明度がありコシがある手触りです'},
            {'key': '1000枚以上', 'value': 'LLDPE#80'},
            {'key': '', 'value': '→半透明でマット調の柔らかい手触りです'},
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
        'name': 'シャツ梱包用',
        'price': '7.0円/袋',
        'quantity': '46,000袋印刷',
        'color_num': '2色印刷',
        'size': '160mm × 140mm',
        'image': 'img/product_detail/common/example/zip_clear_bag_example.jpg',
        'extras': [
            '加工　ノッチ / 角丸'
        ]
    },
    'size_limit': {
        'height': {
            'min': 140,
            'max': 500,
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
            '25': {'name': '2,500', 'value': 2500},
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
                'name': '小物用',
                'value': [
                    {'name': 'height', 'value': 140},
                    {'name': 'width', 'value': 100},
                    {'name': 'top', 'value': 20},
                ],
                'extra': '高さ140mm 幅100mm',
                'image': 'img/external/futureshop/size/zip-clear-bag/accessories.jpg',
                'data': ''
            },
            '2': {
                'name': 'A6サイズ',
                'value': [
                    {'name': 'height', 'value': 170},
                    {'name': 'width', 'value': 120},
                    {'name': 'top', 'value': 20},
                ],
                'extra': '高さ170mm 幅120mm',
                'image': 'img/external/futureshop/size/zip-clear-bag/a6.jpg',
                'data': ''
            },
            '3': {
                'name': ' A5サイズ',
                'value': [
                    {'name': 'height', 'value': 240},
                    {'name': 'width', 'value': 170},
                    {'name': 'top', 'value': 20},
                ],
                'extra': '高さ240mm 幅170mm',
                'image': 'img/external/futureshop/size/zip-clear-bag/a5.jpg',
                'data': ''
            },
            '4': {
                'name': 'A4サイズ',
                'value': [
                    {'name': 'height', 'value': 340},
                    {'name': 'width', 'value': 240},
                    {'name': 'top', 'value': 20},
                ],
                'extra': '高さ340mm 幅240mm',
                'image': 'img/external/futureshop/size/zip-clear-bag/a4.jpg',
                'data': ''
            },
            '5': {
                'name': 'A3サイズ',
                'value': [
                    {'name': 'height', 'value': 480},
                    {'name': 'width', 'value': 340},
                    {'name': 'top', 'value': 20},
                ],
                'extra': '高さ480mm 幅340mm',
                'image': 'img/external/futureshop/size/zip-clear-bag/a3.jpg',
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
    ],
}


print(json.dumps(data, indent=2, ensure_ascii=False))
