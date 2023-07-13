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
        'value': 3000,
        'extra': '',
        'image': '',
    },
    'max_ordering_quantity': {
        'name': '最大注文数',
        'value': 20000,
        'extra': '',
        'image': '',
    },
    'estimated_shipping_date': {
        'name': '納期',
        'value': {
            'first': 45,
            'repeat': 30
        },
        'extra': {
            'first': 'データ確定後1ヶ月半',
            'repeat': '1ヶ月',
        },
        'image': '',
    },
    'can_select_original_size': {
        'name': 'オリジナルサイズ',
        'value': True,
        'extra': '',
        'image': '',
    },
    'print_area': {
        'name': '印刷可能範囲',
        'value': 0,
        'extra': '袋全体',
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
            {'key': 'シール幅', 'value': '5mm'},
            {'key': 'ジップ上', 'value': '30mm'},
            {'key': '材質構成', 'value': 'PET#12/DL/LLDPE#60'},
        ],
        'image': '',
    },
    'choosable_color': {
        'name': '印刷色',
        'value': "フルカラー",
        'extra': '',
        'image': '',
    },
    'example': {
        'value': 21.5,
        'suffix': '円',
        'unit': '枚',
        'lot': 10000
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
        "kadomaru": None,
        "notch": None,
    },
    'option_order': [
        'color_num',
        'kadomaru',
        'notch',
        'size',
        'quantity'
    ],
    'quantity': {
        'name': '注文数',
        'extra': '',
        'required': True,
        'default': '30',
        'image': '',
        'unit': '袋',
        'widget_type': 'radio',
        'options': {
            '30': {'name': '3,000', 'value': 3000},
            '40': {'name': '4,000', 'value': 4000},
            '50': {'name': '5,000', 'value': 5000},
            '75': {'name': '7,500', 'value': 7500},
            '100': {'name': '10,000', 'value': 10000},
            '125': {'name': '12,500', 'value': 12500},
            '150': {'name': '15,000', 'value': 15000},
            '175': {'name': '17,500', 'value': 17500},
            '200': {'name': '20,000', 'value': 20000},
        },
    },
    'size': {
        'name': 'サイズ',
        'extra': 'サイズを選択してください',
        'required': True,
        'default': '1',
        'image': 'img/product_detail/film/size/zip-clear-pressbag/zip-clear-pressbag_original.jpg',
        'widget_type': 'modal-radio',
        'options': {
            '1': {
                'name': '半袖インナー用・Tシャツ用サイズ',
                'value': [
                    {'name': 'height', 'value': 210},
                    {'name': 'width', 'value': 180},
                ],
                'extra': '高さ210mm 幅180mm',
                'image': 'img/product_detail/film/size/zip-clear-pressbag/zip-clear-pressbag_shortsleeve.jpg',
                'data': 'design_templates/flatbag/zip_clear_pressbag/zip_clear_pressbag_t_shirt.ai'
            },
            '2': {
                'name': '長袖インナー用サイズ',
                'value': [
                    {'name': 'height', 'value': 265},
                    {'name': 'width', 'value': 190},
                ],
                'extra': '高さ265mm 幅190mm',
                'image': 'img/product_detail/film/size/zip-clear-pressbag/zip-clear-pressbag_longsleeve.jpg',
                'data': 'design_templates/flatbag/zip_clear_pressbag/zip_clear_pressbag_long_sleeve.ai'
            }
        }
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
            '3': {
                'name': '３色',
                'value': 3,
                'extra': '印刷するデザインに使用する色数が３色の場合です。 生地や材質の色は含みません。',
                'image': 'img/product_detail/common/color_num/color_num_03.png'
            },
            '4': {
                'name': '４色',
                'value': 4,
                'extra': '印刷するデザインに使用する色数が４色の場合です。 生地や材質の色は含みません。',
                'image': 'img/product_detail/common/color_num/color_num_04.png'
            },
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
    'kadomaru': {
        'name': '角丸',
        'extra': '',
        'required': False,
        'default': '1',
        'image': '',
        'widget_type': 'slider-lg',
        'options': {
            '1': {
                'name': '角丸なし',
                'value': False,
                'extra': '角の丸みがありません。',
                'image': 'img/product_detail/film/process/kadomaru_false.jpg'
            },
            '2': {
                'name': '角丸あり',
                'value': True,
                'extra': '世の中で多く見られる形状です。',
                'image': 'img/product_detail/film/process/kadomaru_true.jpg'
            }
        },
        'note': {
            'title': "加工について",
            'sections': [
                {
                    'title': '加工の選択',
                    "layout_type": "grid-list-md",
                    "rows": [
                        {
                            "title": "角丸",
                            "contents": [
                                {
                                    'title': '角丸なし',
                                    'image': 'img/product_detail/film/process/kadomaru_false.jpg',
                                    'body': [
                                        '角の丸みがありません',
                                    ],
                                },
                                {
                                    'title': '角丸あり',
                                    'image': 'img/product_detail/film/process/kadomaru_true.jpg',
                                    'body': [
                                        '世の中で多く見られる形状です',
                                    ],
                                }
                            ]
                        },
                        {
                            "title": "ノッチ",
                            "contents": [
                                {
                                    'title': 'ノッチなし',
                                    'image': 'img/product_detail/film/process/notch_false.jpg',
                                    'body': [
                                        '何も加工しません',
                                    ],
                                },
                                {
                                    'title': 'ノッチあり',
                                    'image': 'img/product_detail/film/process/notch_true.jpg',
                                    'body': [
                                        '切り取りやすくするノッチがつきます',
                                    ],
                                },
                            ]
                        }
                    ]
                }
            ]
        }
    },
    'notch': {
        'name': 'ノッチ',
        'extra': '',
        'required': False,
        'default': '1',
        'image': '',
        'widget_type': 'slider-lg',
        'options': {
            '1': {
                'name': 'ノッチなし',
                'value': False,
                'extra': '何も加工しません。',
                'image': 'img/product_detail/film/process/notch_false.jpg'
            },
            '2': {
                'name': 'ノッチあり',
                'value': True,
                'extra': '切り取りやすくするノッチがつきます。',
                'image': 'img/product_detail/film/process/notch_true.jpg'
            }
        }
    },
}


print(json.dumps(data, indent=2, ensure_ascii=False))
