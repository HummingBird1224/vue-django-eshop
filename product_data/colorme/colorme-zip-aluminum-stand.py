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
        'value': 1000,
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
            'first': 30,
            'repeat': 21
        },
        'extra': {
            'first': 'データ確定後1ヶ月',
            'repeat': '3週間',
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
    'print_area': {
        "name": "印刷可能範囲",
        "value": 0,
        "extra": "袋全体",
        "image": "",
    },
    'notes': {
        'name': '備考',
        'value': '',
        'extra': [
            {'key': 'ジップ上の高さ', 'value': '35mm'},
            {'key': 'ノッチ上の高さ', 'value': '20mm'},
            {'key': '加工', 'value': '角丸加工、ノッチ付き'},
            {'key': '基材構成', 'value': 'PET#12//AL#7//NY#15//LLDPE#40'},
        ],
        'image': '',
    },
    'example': {
        'name': 'プロテイン用',
        'price': '28.7円/袋',
        'quantity': '32,000袋印刷',
        'color_num': '2色印刷',
        'size': '220mm × 310mm + 奥行き112mm',
        'image': 'img/product_detail/common/example/zip_aluminum_stand_example.jpg',
        'extras': [
            '素材　PET//LLDPE',
            '加工　ノッチ / 角丸',
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
        'depth': {
            'min': 0,
            'max': 1000,
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
        'default': '10',
        'image': '',
        'unit': '袋',
        'widget_type': 'radio',
        'options': {
            '10': {'name': '1,000', 'value': 1000},
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
                'name': '粉末100g用',
                'value': [
                    {'name': 'height', 'value': 125},
                    {'name': 'width', 'value': 100},
                    {'name': 'depth', 'value': 56},
                ],
                'extra': '高さ125mm 幅100mm 奥行き56mm',
                'image': 'img/external/colorme/size/zip-aluminum-stand/100g.jpg',
                'data': ''
            },
            '2': {
                'name': '粉末200g用 ',
                'value': [
                    {'name': 'height', 'value': 145},
                    {'name': 'width', 'value': 110},
                    {'name': 'depth', 'value': 65},
                ],
                'extra': '高さ145mm 幅110mm 奥行き65mm',
                'image': 'img/external/colorme/size/zip-aluminum-stand/200g.jpg',
                'data': ''
            },
            '3': {
                'name': '粉末250g用',
                'value': [
                    {'name': 'height', 'value': 155},
                    {'name': 'width', 'value': 120},
                    {'name': 'depth', 'value': 68},
                ],
                'extra': '高さ155mm 幅120mm 奥行き68mm',
                'image': 'img/external/colorme/size/zip-aluminum-stand/250g.jpg',
                'data': ''
            }
        }
    },
    'color_num': {
        'name': '印刷カラー',
        'extra': '',
        'required': True,
        'default': '5',
        'image': '',
        'widget_type': 'slider-sm',
        'options': {
            '5': {
                'name': 'フルカラー',
                'value': -1,
                'extra': '印刷するデザインに使用する色数が５色以上の場合です。 生地や材質の色は含みません。',
                'image': 'img/product_detail/common/color_num/color_num_full.png'
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
        {'name': 'フルカラー', 'image': 'img/external/colorme/color/fullcolor.png'},
    ],
}


print(json.dumps(data, indent=2, ensure_ascii=False))
