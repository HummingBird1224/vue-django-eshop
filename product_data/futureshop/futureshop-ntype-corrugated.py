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
            'first': 21,
            'repeat': 21
        },
        'extra': {
            'first': 'データ確定後2~3週間',
            'repeat': 'データ確定後2~3週間',
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
        'value': True,
    },
    'notes': {
        'name': '備考',
        'value': '',
        'extra': [
            {'key': '厚み', 'value': '1.5mm'},
            {'key': 'サイズ', 'value': '外寸表記です。内寸はおおよそ以下のようになります。'},
            {'key': '①横', 'value': '外寸より11mm小さい'},
            {'key': '②縦', 'value': '外寸より4.5mm小さい'},
            {'key': '③高さ', 'value': '外寸より4mm小さい'},
        ],
        'image': '',
    },
    'example': {
        'name': 'ギフト用梱包箱',
        'price': '53円/箱',
        'quantity': '5,000箱注文',
        'color_num': '1色印刷',
        'size': '190mm × 140mm × 80mm',
        'image': 'img/product_detail/common/example/ntype_corrugated_example.jpg',
        'extras': [
            '両面白色ダンボール',
            '1.5mm 厚',
        ]
    },
    'size_limit': {
        'height': {
            'min': 15,
            'max': 100,
        },
        'width': {
            'min': 150,
            'max': 350,
        },
        'depth': {
            'min': 110,
            'max': 300,
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
        "surface_material": None,
        "design_num": None,
        "print_area_num": None,
    },
    'option_order': [
        'color_num',
        'surface_material',
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
        'unit': '箱',
        'widget_type': 'radio',
        'options': {
            '5': {'name': '50', 'value': 50},
            '10': {'name': '100', 'value': 100},
            '20': {'name': '200', 'value': 200},
            '30': {'name': '300', 'value': 300},
        },
    },
    'size': {
        'name': 'サイズ',
        'extra': 'サイズを選択してください',
        'required': True,
        'default': '1',
        'image': 'img/product_detail/cardboard/size/futureshop-ntype-corrugated/ntype-corrugated_original.jpg',
        'widget_type': 'modal-radio',
        'options': {
            '1': {
                'name': '正方形サイズ',
                'value': [
                    {'name': 'height', 'value': 50},
                    {'name': 'width', 'value': 150},
                    {'name': 'depth', 'value': 150},
                ],
                'extra': '高さ50mm 幅150mm 奥行き150mm',
                'image': 'img/external/futureshop/size/ntype-corrugated/square.jpg',
                'data': ''
            },
            '2': {
                'name': 'A6サイズ',
                'value': [
                    {'name': 'height', 'value': 35},
                    {'name': 'width', 'value': 165},
                    {'name': 'depth', 'value': 100},
                ],
                'extra': '高さ35mm 幅165mm 奥行き100mm',
                'image': 'img/external/futureshop/size/ntype-corrugated/a6.jpg',
                'data': ''
            },
            '3': {
                'name': 'B6サイズ',
                'value': [
                    {'name': 'height', 'value': 35},
                    {'name': 'width', 'value': 190},
                    {'name': 'depth', 'value': 135},
                ],
                'extra': '高さ35mm 幅190mm 奥行き135mm',
                'image': 'img/external/futureshop/size/ntype-corrugated/b6.jpg',
                'data': ''
            },
            '4': {
                'name': 'A5サイズ',
                'value': [
                    {'name': 'height', 'value': 45},
                    {'name': 'width', 'value': 235},
                    {'name': 'depth', 'value': 165},
                ],
                'extra': '高さ45mm 幅235mm 奥行き165mm',
                'image': 'img/external/futureshop/size/ntype-corrugated/a5.jpg',
                'data': ''
            },
            '5': {
                'name': 'A6横長サイズ',
                'value': [
                    {'name': 'height', 'value': 50},
                    {'name': 'width', 'value': 250},
                    {'name': 'depth', 'value': 100},
                ],
                'extra': '高さ50mm 幅250mm 奥行き100mm',
                'image': 'img/external/futureshop/size/ntype-corrugated/a6_wide.jpg',
                'data': ''
            },
            '6': {
                'name': 'B5サイズ',
                'value': [
                    {'name': 'height', 'value': 60},
                    {'name': 'width', 'value': 275},
                    {'name': 'depth', 'value': 200},
                ],
                'extra': '高さ60mm 幅275mm 奥行き200mm',
                'image': 'img/external/futureshop/size/ntype-corrugated/b5.jpg',
                'data': ''
            },
            '7': {
                'name': 'B6横長サイズ',
                'value': [
                    {'name': 'height', 'value': 70},
                    {'name': 'width', 'value': 285},
                    {'name': 'depth', 'value': 135},
                ],
                'extra': '高さ70mm 幅285mm 奥行き135mm',
                'image': 'img/external/futureshop/size/ntype-corrugated/b6_wide.jpg',
                'data': ''
            },
            '8': {
                'name': 'A4サイズ',
                'value': [
                    {'name': 'height', 'value': 40},
                    {'name': 'width', 'value': 330},
                    {'name': 'depth', 'value': 230},
                ],
                'extra': '高さ40mm 幅330mm 奥行き230mm',
                'image': 'img/external/futureshop/size/ntype-corrugated/a4.jpg',
                'data': ''
            },
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
                        },
                        {
                            'title': 'フルカラー',
                            'image': 'img/product_detail/common/color_num/color_num_full.png'
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
    'surface_material': {
        'name': '表面生地',
        'extra': '',
        'required': False,
        'default': '1',
        'image': '',
        'widget_type': 'slider-lg',
        'options': {
            '1': {
                'name': 'クラフト',
                'value': 'normal',
                'extra': 'ダンボールそのままの素材です。\n' \
                         'コストを抑えられますが、段目が見えるなど完成度は他と劣ります。\n' \
                         '印刷に使える色に制限があります。',
                'image': 'img/product_detail/cardboard/surface_material/ntype-corrugated/material_1_sm.jpg'
            },
            '2': {
                'name': '白',
                'value': 'white',
                'extra': 'コストを抑えて上質感を出せる素材です。\n' \
                         '印刷に使える色に制限があります。',
                'image': 'img/product_detail/cardboard/surface_material/ntype-corrugated/material_2_sm.jpg'
            },
        },
    },
    'design_num': {
        'name': '印刷するデザインの数',
        'extra': '',
        'required': True,
        'default': '1',
        'image': '',
        'widget_type': 'slider-sm',
        "condition": {
            "key": "print_area_num",
            "operator": "equal",
            "value": 2,
        },
        'options': {
            '1': {
                'name': '１つ',
                'value': 1,
                'extra': '',
                'image': ''
            },
            '2': {
                'name': '２つ',
                'value': 2,
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
            '2': {
                'name': '２面',
                'value': 2,
                'extra': '',
                'image': ''
            },
        },
    },
    'choosable_color': [
        {'name': '白', 'image': 'img/external/futureshop/color/white.png'},
        {'name': '黒', 'image': 'img/external/futureshop/color/black.png'},
        {'name': '青', 'image': 'img/external/futureshop/color/blue.png'},
        {'name': '赤', 'image': 'img/external/futureshop/color/red.png'},
        {'name': '緑', 'image': 'img/external/futureshop/color/green.png'},
    ],
    # EASY DRAFT
    'easy_draft': {
        # height_width_depth
        '50_150_150_1': {  # square
            'pdf_size': {  # unit mm
                'height': 260,
                'width': 650,
            },
            'pdf_color': {
                'background': "#CBA878",
                'border': '#FFFFFF',
            },
            "image_size": {
                "width": 1660,
                "height": 1040,
            },
            'print_area': [
                {
                    "name": "正面",
                    "id": "A",
                    "is_printable": True,
                    "image": "img/easy_draft/products/futureshop-ntype-corrugated/square/01.png",
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/square/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 638,
                                "y": 502,
                            },
                            "end": {  # bottom right
                                "x": 1064,
                                "y": 828,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 150,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "左面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/square/02.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/square/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/square/03.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/square/thumbnail/03.png",
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/square/04.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/square/thumbnail/04.png",
                },
            ],
        },
        '35_165_100_1': {  # a6
            'pdf_size': {  # unit mm
                'height': 260,
                'width': 650,
            },
            'pdf_color': {
                'background': "#CBA878",
                'border': '#FFFFFF',
            },
            "image_size": {
                "width": 1660,
                "height": 1040,
            },
            'print_area': [
                {
                    "name": "正面",
                    "id": "A",
                    "is_printable": True,
                    "image": "img/easy_draft/products/futureshop-ntype-corrugated/a6/01.png",
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a6/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 604,
                                "y": 638,
                            },
                            "end": {  # bottom right
                                "x": 1078,
                                "y": 898,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 165,
                                "y": 100,
                            },
                        }
                    }
                },
                {
                    "name": "左面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a6/02.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a6/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a6/03.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a6/thumbnail/03.png",
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a6/04.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a6/thumbnail/04.png",
                },
            ],
        },
        '35_190_135_1': {  # b6
            'pdf_size': {  # unit mm
                'height': 260,
                'width': 650,
            },
            'pdf_color': {
                'background': "#CBA878",
                'border': '#FFFFFF',
            },
            "image_size": {
                "width": 1660,
                "height": 1040,
            },
            'print_area': [
                {
                    "name": "正面",
                    "id": "A",
                    "is_printable": True,
                    "image": "img/easy_draft/products/futureshop-ntype-corrugated/b6/01.png",
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b6/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 536,
                                "y": 560,
                            },
                            "end": {  # bottom right
                                "x": 1092,
                                "y": 886,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 190,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "左面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/b6/02.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b6/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/b6/03.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b6/thumbnail/03.png",
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/b6/04.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b6/thumbnail/04.png",
                },
            ],
        },
        '45_235_165_1': {  # a5
            'pdf_size': {  # unit mm
                'height': 260,
                'width': 650,
            },
            'pdf_color': {
                'background': "#CBA878",
                'border': '#FFFFFF',
            },
            "image_size": {
                "width": 1660,
                "height": 1040,
            },
            'print_area': [
                {
                    "name": "正面",
                    "id": "A",
                    "is_printable": True,
                    "image": "img/easy_draft/products/futureshop-ntype-corrugated/a5/01.png",
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a5/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 506,
                                "y": 440,
                            },
                            "end": {  # bottom right
                                "x": 1128,
                                "y": 766,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 210,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "左面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a5/02.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a5/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a5/03.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a5/thumbnail/03.png",
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a5/04.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a5/thumbnail/04.png",
                },
            ],
        },
        '50_250_100_1': {  # a6 wide
            'pdf_size': {  # unit mm
                'height': 260,
                'width': 650,
            },
            'pdf_color': {
                'background': "#CBA878",
                'border': '#FFFFFF',
            },
            "image_size": {
                "width": 1660,
                "height": 1040,
            },
            'print_area': [
                {
                    "name": "正面",
                    "id": "A",
                    "is_printable": True,
                    "image": "img/easy_draft/products/futureshop-ntype-corrugated/a6_wide/01.png",
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a6_wide/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 498,
                                "y": 616,
                            },
                            "end": {  # bottom right
                                "x": 1120,
                                "y": 876,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 210,
                                "y": 100,
                            },
                        }
                    }
                },
                {
                    "name": "左面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a6_wide/02.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a6_wide/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a6_wide/03.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a6_wide/thumbnail/03.png",
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a6_wide/04.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a6_wide/thumbnail/04.png",
                },
            ],
        },
        '60_275_200_1': {  # b5
            'pdf_size': {  # unit mm
                'height': 260,
                'width': 650,
            },
            'pdf_color': {
                'background': "#CBA878",
                'border': '#FFFFFF',
            },
            "image_size": {
                "width": 1660,
                "height": 1040,
            },
            'print_area': [
                {
                    "name": "正面",
                    "id": "A",
                    "is_printable": True,
                    "image": "img/easy_draft/products/futureshop-ntype-corrugated/b5/01.png",
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b5/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 496,
                                "y": 450,
                            },
                            "end": {  # bottom right
                                "x": 1118,
                                "y": 776,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 210,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "左面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/b5/02.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b5/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/b5/03.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b5/thumbnail/03.png",
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/b5/04.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b5/thumbnail/04.png",
                },
            ],
        },
        '70_285_135_1': {  # b6 wide
            'pdf_size': {  # unit mm
                'height': 260,
                'width': 650,
            },
            'pdf_color': {
                'background': "#CBA878",
                'border': '#FFFFFF',
            },
            "image_size": {
                "width": 1660,
                "height": 1040,
            },
            'print_area': [
                {
                    "name": "正面",
                    "id": "A",
                    "is_printable": True,
                    "image": "img/easy_draft/products/futureshop-ntype-corrugated/b6_wide/01.png",
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b6_wide/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 552,
                                "y": 578,
                            },
                            "end": {  # bottom right
                                "x": 1108,
                                "y": 904,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 190,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "左面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/b6_wide/02.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b6_wide/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/b6_wide/03.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b6_wide/thumbnail/03.png",
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/b6_wide/04.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b6_wide/thumbnail/04.png",
                },
            ],
        },
        '40_330_230_1': {  # a4
            'pdf_size': {  # unit mm
                'height': 260,
                'width': 650,
            },
            'pdf_color': {
                'background': "#CBA878",
                'border': '#FFFFFF',
            },
            "image_size": {
                "width": 1660,
                "height": 1040,
            },
            'print_area': [
                {
                    "name": "正面",
                    "id": "A",
                    "is_printable": True,
                    "image": "img/easy_draft/products/futureshop-ntype-corrugated/a4/01.png",
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a4/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 514,
                                "y": 432,
                            },
                            "end": {  # bottom right
                                "x": 1136,
                                "y": 758,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 190,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "左面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a4/02.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a4/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a4/03.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a4/thumbnail/03.png",
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a4/04.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a4/thumbnail/04.png",
                },
            ],
        },

        # 2 print areas
        '50_150_150_2': {  # square
            'pdf_size': {  # unit mm
                'height': 260,
                'width': 650,
            },
            'pdf_color': {
                'background': "#CBA878",
                'border': '#FFFFFF',
            },
            "image_size": {
                "width": 1660,
                "height": 1040,
            },
            'print_area': [
                {
                    "name": "正面",
                    "id": "A",
                    "is_printable": True,
                    "image": "img/easy_draft/products/futureshop-ntype-corrugated/square/01.png",
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/square/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 638,
                                "y": 502,
                            },
                            "end": {  # bottom right
                                "x": 1064,
                                "y": 828,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 150,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "左面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/square/02.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/square/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": True,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/square/03.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/square/thumbnail/03.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 640,
                                "y": 504,
                            },
                            "end": {  # bottom right
                                "x": 1066,
                                "y": 830,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 170,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 300,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/square/04.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/square/thumbnail/04.png",
                },
            ],
        },
        '35_165_100_2': {  # a6
            'pdf_size': {  # unit mm
                'height': 260,
                'width': 650,
            },
            'pdf_color': {
                'background': "#CBA878",
                'border': '#FFFFFF',
            },
            "image_size": {
                "width": 1660,
                "height": 1040,
            },
            'print_area': [
                {
                    "name": "正面",
                    "id": "A",
                    "is_printable": True,
                    "image": "img/easy_draft/products/futureshop-ntype-corrugated/a6/01.png",
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a6/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 604,
                                "y": 638,
                            },
                            "end": {  # bottom right
                                "x": 1078,
                                "y": 898,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 165,
                                "y": 100,
                            },
                        }
                    }
                },
                {
                    "name": "左面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a6/02.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a6/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": True,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a6/03.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a6/thumbnail/03.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 604,
                                "y": 636,
                            },
                            "end": {  # bottom right
                                "x": 1078,
                                "y": 896,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 185,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 330,
                                "y": 100,
                            },
                        }
                    }
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a6/04.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a6/thumbnail/04.png",
                },
            ],
        },
        '35_190_135_2': {  # b6
            'pdf_size': {  # unit mm
                'height': 260,
                'width': 650,
            },
            'pdf_color': {
                'background': "#CBA878",
                'border': '#FFFFFF',
            },
            "image_size": {
                "width": 1660,
                "height": 1040,
            },
            'print_area': [
                {
                    "name": "正面",
                    "id": "A",
                    "is_printable": True,
                    "image": "img/easy_draft/products/futureshop-ntype-corrugated/b6/01.png",
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b6/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 536,
                                "y": 560,
                            },
                            "end": {  # bottom right
                                "x": 1092,
                                "y": 886,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 190,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "左面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/b6/02.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b6/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": True,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/b6/03.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b6/thumbnail/03.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 544,
                                "y": 544,
                            },
                            "end": {  # bottom right
                                "x": 1100,
                                "y": 870,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 210,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 380,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/b6/04.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b6/thumbnail/04.png",
                },
            ],
        },
        '45_235_165_2': {  # a5
            'pdf_size': {  # unit mm
                'height': 260,
                'width': 650,
            },
            'pdf_color': {
                'background': "#CBA878",
                'border': '#FFFFFF',
            },
            "image_size": {
                "width": 1660,
                "height": 1040,
            },
            'print_area': [
                {
                    "name": "正面",
                    "id": "A",
                    "is_printable": True,
                    "image": "img/easy_draft/products/futureshop-ntype-corrugated/a5/01.png",
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a5/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 506,
                                "y": 440,
                            },
                            "end": {  # bottom right
                                "x": 1128,
                                "y": 766,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 210,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "左面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a5/02.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a5/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": True,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a5/03.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a5/thumbnail/03.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 506,
                                "y": 440,
                            },
                            "end": {  # bottom right
                                "x": 1128,
                                "y": 766,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 230,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 420,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a5/04.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a5/thumbnail/04.png",
                },
            ],
        },
        '50_250_100_2': {  # a6 wide
            'pdf_size': {  # unit mm
                'height': 260,
                'width': 650,
            },
            'pdf_color': {
                'background': "#CBA878",
                'border': '#FFFFFF',
            },
            "image_size": {
                "width": 1660,
                "height": 1040,
            },
            'print_area': [
                {
                    "name": "正面",
                    "id": "A",
                    "is_printable": True,
                    "image": "img/easy_draft/products/futureshop-ntype-corrugated/a6_wide/01.png",
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a6_wide/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 498,
                                "y": 616,
                            },
                            "end": {  # bottom right
                                "x": 1120,
                                "y": 876,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 210,
                                "y": 100,
                            },
                        }
                    }
                },
                {
                    "name": "左面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a6_wide/02.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a6_wide/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": True,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a6_wide/03.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a6_wide/thumbnail/03.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 502,
                                "y": 606,
                            },
                            "end": {  # bottom right
                                "x": 1124,
                                "y": 866,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 230,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 420,
                                "y": 100,
                            },
                        }
                    }
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a6_wide/04.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a6_wide/thumbnail/04.png",
                },
            ],
        },
        '60_275_200_2': {  # b5
            'pdf_size': {  # unit mm
                'height': 260,
                'width': 650,
            },
            'pdf_color': {
                'background': "#CBA878",
                'border': '#FFFFFF',
            },
            "image_size": {
                "width": 1660,
                "height": 1040,
            },
            'print_area': [
                {
                    "name": "正面",
                    "id": "A",
                    "is_printable": True,
                    "image": "img/easy_draft/products/futureshop-ntype-corrugated/b5/01.png",
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b5/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 496,
                                "y": 450,
                            },
                            "end": {  # bottom right
                                "x": 1118,
                                "y": 776,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 210,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "左面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/b5/02.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b5/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": True,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/b5/03.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b5/thumbnail/03.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 506,
                                "y": 446,
                            },
                            "end": {  # bottom right
                                "x": 1128,
                                "y": 772,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 230,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 420,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/b5/04.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b5/thumbnail/04.png",
                },
            ],
        },
        '70_285_135_2': {  # b6 wide
            'pdf_size': {  # unit mm
                'height': 260,
                'width': 650,
            },
            'pdf_color': {
                'background': "#CBA878",
                'border': '#FFFFFF',
            },
            "image_size": {
                "width": 1660,
                "height": 1040,
            },
            'print_area': [
                {
                    "name": "正面",
                    "id": "A",
                    "is_printable": True,
                    "image": "img/easy_draft/products/futureshop-ntype-corrugated/b6_wide/01.png",
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b6_wide/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 552,
                                "y": 578,
                            },
                            "end": {  # bottom right
                                "x": 1108,
                                "y": 904,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 190,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "左面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/b6_wide/02.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b6_wide/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": True,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/b6_wide/03.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b6_wide/thumbnail/03.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 556,
                                "y": 556,
                            },
                            "end": {  # bottom right
                                "x": 1112,
                                "y": 882,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 210,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 380,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/b6_wide/04.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/b6_wide/thumbnail/04.png",
                },
            ],
        },
        '40_330_230_2': {  # a4
            'pdf_size': {  # unit mm
                'height': 260,
                'width': 650,
            },
            'pdf_color': {
                'background': "#CBA878",
                'border': '#FFFFFF',
            },
            "image_size": {
                "width": 1660,
                "height": 1040,
            },
            'print_area': [
                {
                    "name": "正面",
                    "id": "A",
                    "is_printable": True,
                    "image": "img/easy_draft/products/futureshop-ntype-corrugated/a4/01.png",
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a4/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 514,
                                "y": 432,
                            },
                            "end": {  # bottom right
                                "x": 1136,
                                "y": 758,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 190,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "左面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a4/02.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a4/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": True,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a4/03.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a4/thumbnail/03.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 514,
                                "y": 432,
                            },
                            "end": {  # bottom right
                                "x": 1136,
                                "y": 758,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 210,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 380,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/futureshop-ntype-corrugated/a4/04.png',
                    "thumbnail": "img/easy_draft/products/futureshop-ntype-corrugated/a4/thumbnail/04.png",
                },
            ],
        },
    },
}


print(json.dumps(data, indent=2, ensure_ascii=False))
