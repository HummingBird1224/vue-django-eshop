import json

data = {
    'contact_required': {
        'name': 'お問い合わせ',
        'value': True,
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
        'value': 300000,
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
        'value': True,
        'extra': '',
        'image': '',
    },
    'print_area': {
        'name': '印刷可能範囲',
        'value': 5,
        'extra': '端から5mmの余白を開ける必要があり、その部分は印刷ができません。',
        'image': 'img/product_detail/film/print_area/5mm.jpg',
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
            {'key': '基材構成', 'value': 'LDPE'},
            {'key': 'リップ長さ', 'value': '30 ~ 40mm'},
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
        'value': 56.3,
        'suffix': '円',
        'unit': '枚',
        'lot': 1000
    },
    'size_limit': {
        'height': {
            'min': 140,
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
    },
    'option_order': [
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
                'name': 'A4サイズ',
                'value': [
                    {'name': 'height', 'value': 305},
                    {'name': 'width', 'value': 225},
                    {'name': 'lip', 'value': 40},
                ],
                'extra': '高さ305mm 幅225mm',
                'data': 'design_templates/flatbag/tape_bag/tape_bag_a4.ai'
            },
            '2': {
                'name': ' A5サイズ',
                'value': [
                    {'name': 'height', 'value': 220},
                    {'name': 'width', 'value': 160},
                    {'name': 'lip', 'value': 30},
                ],
                'extra': '高さ220mm 幅160mm',
                'data': 'design_templates/flatbag/tape_bag/tape_bag_a5.ai'
            },
            '3': {
                'name': 'A6サイズ',
                'value': [
                    {'name': 'height', 'value': 155},
                    {'name': 'width', 'value': 110},
                    {'name': 'lip', 'value': 30},
                ],
                'extra': '高さ155mm 幅110mm',
                'data': 'design_templates/flatbag/tape_bag/tape_bag_a6.ai'
            },
            '4': {
                'name': 'カットソー・シャツサイズ',
                'value': [
                    {'name': 'height', 'value': 370},
                    {'name': 'width', 'value': 250},
                    {'name': 'lip', 'value': 40},
                ],
                'extra': '高さ370mm 幅250mm',
                'data': 'design_templates/flatbag/tape_bag/tape_bag_shirt.ai'
            },
            '5': {
                'name': 'セーター・ニットサイズ',
                'value': [
                    {'name': 'height', 'value': 400},
                    {'name': 'width', 'value': 300},
                    {'name': 'lip', 'value': 40},
                ],
                'extra': '高さ400mm 幅300mm',
                'data': 'design_templates/flatbag/tape_bag/tape_bag_sweater.ai'
            },
            '6': {
                'name': 'パンツサイズ',
                'value': [
                    {'name': 'height', 'value': 550},
                    {'name': 'width', 'value': 400},
                    {'name': 'lip', 'value': 40},
                ],
                'extra': '高さ550mm 幅400mm',
                'data': 'design_templates/flatbag/tape_bag/tape_bag_pants.ai'
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
                            'image': 'img/product_detail/film/print_area/5mm.jpg',
                            "body": [
                                "端から5mmの余白を開ける必要があり、その部分は印刷ができません。",
                            ]
                        },
                    ]
                },
            ]
        }
    },
    'material': {
        'name': '材質',
        'extra': '表面の色は下記のものだけ利用できます',
        'required': False,
        'default': '1',
        'image': '',
        'widget_type': 'slider-lg',
        'options': {
            '1': {
                'name': '白(ホワイト)',
                'value': 'white',
                'extra': 'くすんだグレーに近い色です。',
                'image': 'img/product_detail/film/material/white.png'
            },
        },
        'note': {
            'title': '材質について',
            'sections': [
                {
                    'title': '材質の選択',
                    'layout_type': 'horizontal-list-md',
                    'summary': {
                        'title': '手触りや光沢の違いで、高級感の違いが生まれます',
                    },
                    'contents': [
                        {
                            'title': '白(ホワイト)',
                            'image': 'img/product_detail/film/material/white.png',
                            'body': [
                                'くすんだグレーに近い色です。',
                            ]
                        },
                    ]
                },
            ]
        }
    },
}


print(json.dumps(data, indent=2, ensure_ascii=False))
