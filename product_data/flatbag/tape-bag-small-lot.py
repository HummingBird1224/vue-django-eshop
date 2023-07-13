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
        'value': True,
        'extra': '',
        'image': '',
    },
    'min_ordering_quantity': {
        'name': '最小注文数',
        'value': 500,
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
            'first': 21,
            'repeat': 14
        },
        'extra': {
            'first': 'データ確定後3週間',
            'repeat': '2週間',
        },
        'image': '',
    },
    'can_select_original_size': {
        'name': 'オリジナルサイズ',
        'value': False,
        'extra': '',
        'image': '',
    },
    'print_area': {
        'name': '印刷可能範囲',
        'value': 5,
        'extra': '端から5mmの余白を開ける必要があり、その部分は印刷ができません。',
        'image': 'img/product_detail/film/print_area/5mm.jpg',
    },
    'notes': {
        'name': '備考',
        'value': '',
        'extra': [
            {'key': 'フタの長さ', 'value': '40mm'},
            {'key': '表面色', 'value': '白色(くすんだグレーに近い色です)'},
            {'key': '内面色', 'value': '黒色'},
            {'key': '基材構成', 'value': 'HDPE//LDPE ※厚さはサイズによって変わります。'},
        ],
        'image': '',
    },
    'choosable_color': {
        'name': '印刷色',
        'value': "1色(pantoneから選択)",
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
        'value': True,
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
        'size': [
            "height",
            "width",
        ],
        "color_num": None,
        "quantity": None,
        "design_num": None,
        "print_area_num": None,
    },
    'option_order': [
        'color_num',
        'print_area_num',
        'design_num',
        'size',
        'quantity'
    ],
    'quantity': {
        'name': '注文数',
        'extra': '',
        'required': True,
        'default': '5',
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
        'image': 'img/product_detail/film/size/tape-bag-small-lot/tape-bag_original.jpg',
        'widget_type': 'modal-radio',
        'options': {
            '1': {
                'name': 'A4サイズ',
                'value': [
                    {'name': 'height', 'value': 310},
                    {'name': 'width', 'value': 220},
                    {'name': 'lip', 'value': 40},
                ],
                'extra': '高さ310mm 幅220mm',
                'image': 'img/product_detail/film/size/tape-bag-small-lot/tape-bag_a4.jpg',
                'data': 'design_templates/flatbag/tape_bag_small_lot/tape_bag_a4.ai'
            },
            '2': {
                'name': 'クリックポスト',
                'value': [
                    {'name': 'height', 'value': 340},
                    {'name': 'width', 'value': 250},
                    {'name': 'lip', 'value': 40},
                ],
                'extra': '高さ340mm 幅250mm',
                'image': 'img/product_detail/film/size/tape-bag-small-lot/tape-bag_clickpost.jpg',
                'data': 'design_templates/flatbag/tape_bag_small_lot/tape_bag_clickpost.ai'
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
    'design_num': {
        'name': '印刷するデザインの数',
        'extra': '',
        'required': True,
        'default': '1',
        'image': '',
        'widget_type': 'slider-sm',
        'options': {
            '1': {
                'name': '１つ',
                'value': 1,
                'extra': '',
                'image': ''
            },
        },
    },
    'print_area_num': {
        'name': '印刷する面数',
        'extra': '',
        'required': True,
        'default': '1',
        'image': '',
        'widget_type': 'slider-sm',
        'options': {
            '1': {
                'name': '１面',
                'value': 1,
                'extra': '',
                'image': ''
            },
        },
    },
    # EASY DRAFT
    'easy_draft': {
        # height_width_depth
        '310_220_1': {  # a4
            'pdf_size': {  # unit mm
                'height': 330,
                'width': 240,
            },
            'pdf_color': {
                'background': "#FFFFFF",
                'border': '#000000',
            },
            "image_size": {
                "width": 1660,
                "height": 1040,
            },
            'print_area': [
                {
                    "name": "前面",
                    "id": "A",
                    "is_printable": True,
                    "image": "img/easy_draft/products/tape-bag-small-lot/a4/01.png",
                    "thumbnail": "img/easy_draft/products/tape-bag-small-lot/a4/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 598,
                                "y": 270,
                            },
                            "end": {  # bottom right
                                "x": 1043,
                                "y": 915,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 220,
                                "y": 310,
                            },
                        }
                    }
                },
                {
                    "name": "背面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/tape-bag-small-lot/a4/02.png',
                    "thumbnail": "img/easy_draft/products/tape-bag-small-lot/a4/thumbnail/02.png",
                },
            ],
        },
        '340_250_1': {  # clickpost
            'pdf_size': {  # unit mm
                'height': 360,
                'width': 270,
            },
            'pdf_color': {
                'background': "#FFFFFF",
                'border': '#000000',
            },
            "image_size": {
                "width": 1660,
                "height": 1040,
            },
            'print_area': [
                {
                    "name": "前面",
                    "id": "A",
                    "is_printable": True,
                    "image": "img/easy_draft/products/tape-bag-small-lot/clickpost/01.png",
                    "thumbnail": "img/easy_draft/products/tape-bag-small-lot/clickpost/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 606,
                                "y": 263,
                            },
                            "end": {  # bottom right
                                "x": 1063,
                                "y": 899,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 250,
                                "y": 340,
                            },
                        }
                    }
                },
                {
                    "name": "背面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/tape-bag-small-lot/a5/02.png',
                    "thumbnail": "img/easy_draft/products/tape-bag-small-lot/a5/thumbnail/02.png",
                },
            ],
        },
    }
}


print(json.dumps(data, indent=2, ensure_ascii=False))
