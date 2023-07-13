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
        'value': False,
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
        'value': True,
    },
    'notes': {
        'name': '備考',
        'value': '',
        'extra': [
            {'key': 'ジップ上の高さ', 'value': '35mm'},
            {'key': 'ノッチ上の高さ', 'value': '20mm'},
            {'key': '加工', 'value': '角丸加工、ノッチ付き'},
            {'key': '基本構成', 'value': 'PET#12//AL#7//NY#15//LLDPE#40'},
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
        'value': 107.5,
        'suffix': '円',
        'unit': '枚',
        'lot': 1000
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
        'extra': '',
        'required': True,
        'default': '1',
        'image': 'img/product_detail/film/size/zip-aluminum-bag-small-lot/zip-aluminum-bag_original.jpg',
        'widget_type': 'modal-radio',
        'options': {
            '1': {
                'name': '粉末50g用',
                'value': [
                    {'name': 'height', 'value': 125},
                    {'name': 'width', 'value': 100},
                ],
                'extra': '高さ125mm 幅100mm',
                'image': 'img/product_detail/film/size/zip-aluminum-bag-small-lot/zip-aluminum-bag_50g.jpg',
                'data': 'design_templates/flatbag/zip_aluminum_bag_small_lot/zip_aluminum_bag_50g.ai'
            },
            '2': {
                'name': '粉末150g用',
                'value': [
                    {'name': 'height', 'value': 155},
                    {'name': 'width', 'value': 120},
                ],
                'extra': '高さ155mm 幅120mm',
                'image': 'img/product_detail/film/size/zip-aluminum-bag-small-lot/zip-aluminum-bag_150g.jpg',
                'data': 'design_templates/flatbag/zip_aluminum_bag_small_lot/zip_aluminum_bag_150g.ai'
            },
            '3': {
                'name': '粉末200g用',
                'value': [
                    {'name': 'height', 'value': 165},
                    {'name': 'width', 'value': 130},
                ],
                'extra': '高さ165mm 幅130mm',
                'image': 'img/product_detail/film/size/zip-aluminum-bag-small-lot/zip-aluminum-bag_200g.jpg',
                'data': 'design_templates/flatbag/zip_aluminum_bag_small_lot/zip_aluminum_bag_200g.ai'
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
        '160_100_1': {  # 50g
            'pdf_size': {  # unit mm
                'height': 200,
                'width': 140,
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
                    "image": "img/easy_draft/products/zip-aluminum-bag-small-lot/50g/01.png",
                    "thumbnail": "img/easy_draft/products/zip-aluminum-bag-small-lot/50g/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 710,
                                "y": 238,
                            },
                            "end": {  # bottom right
                                "x": 993,
                                "y": 819,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 120,
                                "y": 180,
                            },
                        }
                    }
                },
                {
                    "name": "背面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/zip-aluminum-bag-small-lot/50g/02.png',
                    "thumbnail": "img/easy_draft/products/zip-aluminum-bag-small-lot/50g/thumbnail/02.png",
                },
            ],
        },
        '155_120_1': {  # 150g
            'pdf_size': {  # unit mm
                'height': 200,
                'width': 160,
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
                    "image": "img/easy_draft/products/zip-aluminum-bag-small-lot/150g/01.png",
                    "thumbnail": "img/easy_draft/products/zip-aluminum-bag-small-lot/150g/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 674,
                                "y": 219,
                            },
                            "end": {  # bottom right
                                "x": 1050,
                                "y": 705,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 140,
                                "y": 175,
                            },
                        }
                    }
                },
                {
                    "name": "背面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/zip-aluminum-bag-small-lot/150g/02.png',
                    "thumbnail": "img/easy_draft/products/zip-aluminum-bag-small-lot/150g/thumbnail/02.png",
                },
            ],
        },
        '165_130_1': {  # 200g
            'pdf_size': {  # unit mm
                'height': 220,
                'width': 180,
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
                    "image": "img/easy_draft/products/zip-aluminum-bag-small-lot/200g/01.png",
                    "thumbnail": "img/easy_draft/products/zip-aluminum-bag-small-lot/200g/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 656,
                                "y": 229,
                            },
                            "end": {  # bottom right
                                "x": 1064,
                                "y": 747,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 150,
                                "y": 185,
                            },
                        }
                    }
                },
                {
                    "name": "背面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/zip-aluminum-bag-small-lot/200g/02.png',
                    "thumbnail": "img/easy_draft/products/zip-aluminum-bag-small-lot/200g/thumbnail/02.png",
                },
            ],
        },
    }
}


print(json.dumps(data, indent=2, ensure_ascii=False))
