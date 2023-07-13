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
            {'key': '厚み', 'value': '100サイズ横長以外は3mm、100サイズ横長は5mmです。'},
            {'key': 'サイズ', 'value': '外寸表記です。'},
            {'key': '①横', 'value': '外寸より6mm小さい(100サイズ横長は10mm)'},
            {'key': '②縦', 'value': '外寸より6mm小さい(100サイズ横長は10mm)'},
            {'key': '③高さ', 'value': '外寸より10mm小さい(100サイズ横長は15mm)'},
        ],
        'image': '',
    },
    'example': {
        'name': '配送箱',
        'price': '53円/箱',
        'quantity': '1,000箱注文',
        'color_num': '1色印刷',
        'size': '370mm × 270mm × 175mm',
        'image': 'img/product_detail/common/example/atype_example.jpg',
        'extras': [
        ]
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
        'unit': '箱',
        'widget_type': 'radio',
        'options': {
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
                'image': 'img/external/base/size/atype/60.jpg',
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
                'image': 'img/external/base/size/atype/80_square.jpg',
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
                'image': 'img/external/base/size/atype/80.jpg',
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
                'image': 'img/external/base/size/atype/80_wide.jpg',
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
                'image': 'img/external/base/size/atype/100.jpg',
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
                'image': 'img/external/base/size/atype/100_wide.jpg',
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
        {'name': '白', 'image': 'img/external/base/color/white.png'},
        {'name': '黒', 'image': 'img/external/base/color/black.png'},
        {'name': '青', 'image': 'img/external/base/color/blue.png'},
        {'name': '赤', 'image': 'img/external/base/color/red.png'},
        {'name': '緑', 'image': 'img/external/base/color/green.png'},
    ],
    # EASY DRAFT
    'easy_draft': {
        # height_width_depth
        '120_250_210_1': {  # 60
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
                    "image": "img/easy_draft/products/base-atype/60/01.png",
                    "thumbnail": "img/easy_draft/products/base-atype/60/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 532,
                                "y": 622,
                            },
                            "end": {  # bottom right
                                "x": 1124,
                                "y": 932,
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
                    "image": 'img/easy_draft/products/base-atype/60/02.png',
                    "thumbnail": "img/easy_draft/products/base-atype/60/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/base-atype/60/03.png',
                    "thumbnail": "img/easy_draft/products/base-atype/60/thumbnail/03.png",
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/base-atype/60/04.png',
                    "thumbnail": "img/easy_draft/products/base-atype/60/thumbnail/04.png",
                },
            ],
        },
        '190_250_190_1': {  # 60 wide
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
                    "image": "img/easy_draft/products/base-atype/60_wide/01.png",
                    "thumbnail": "img/easy_draft/products/base-atype/60_wide/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 532,
                                "y": 562,
                            },
                            "end": {  # bottom right
                                "x": 1124,
                                "y": 872,
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
                    "image": 'img/easy_draft/products/base-atype/60_wide/02.png',
                    "thumbnail": "img/easy_draft/products/base-atype/60_wide/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/base-atype/60_wide/03.png',
                    "thumbnail": "img/easy_draft/products/base-atype/60_wide/thumbnail/03.png",
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/base-atype/60_wide/04.png',
                    "thumbnail": "img/easy_draft/products/base-atype/60_wide/thumbnail/04.png",
                },
            ],
        },
        '150_310_220_1': {  # 80
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
                    "image": "img/easy_draft/products/base-atype/80/01.png",
                    "thumbnail": "img/easy_draft/products/base-atype/80/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 532,
                                "y": 600,
                            },
                            "end": {  # bottom right
                                "x": 1124,
                                "y": 910,
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
                    "image": 'img/easy_draft/products/base-atype/80/02.png',
                    "thumbnail": "img/easy_draft/products/base-atype/80/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/base-atype/80/03.png',
                    "thumbnail": "img/easy_draft/products/base-atype/80/thumbnail/03.png",
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/base-atype/80/04.png',
                    "thumbnail": "img/easy_draft/products/base-atype/80/thumbnail/04.png",
                },
            ],
        },
        '100_400_200_1': {  # 80 wide
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
                    "image": "img/easy_draft/products/base-atype/80_wide/01.png",
                    "thumbnail": "img/easy_draft/products/base-atype/80_wide/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 534,
                                "y": 748,
                            },
                            "end": {  # bottom right
                                "x": 1126,
                                "y": 996,
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
                    "image": 'img/easy_draft/products/base-atype/80_wide/02.png',
                    "thumbnail": "img/easy_draft/products/base-atype/80_wide/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/base-atype/80_wide/03.png',
                    "thumbnail": "img/easy_draft/products/base-atype/80_wide/thumbnail/03.png",
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/base-atype/80_wide/04.png',
                    "thumbnail": "img/easy_draft/products/base-atype/80_wide/thumbnail/04.png",
                },
            ],
        },
        '250_350_300_1': {  # 100
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
                    "image": "img/easy_draft/products/base-atype/100/01.png",
                    "thumbnail": "img/easy_draft/products/base-atype/100/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 532,
                                "y": 464,
                            },
                            "end": {  # bottom right
                                "x": 1124,
                                "y": 774,
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
                    "image": 'img/easy_draft/products/base-atype/100/02.png',
                    "thumbnail": "img/easy_draft/products/base-atype/100/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/base-atype/100/03.png',
                    "thumbnail": "img/easy_draft/products/base-atype/100/thumbnail/03.png",
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/base-atype/100/04.png',
                    "thumbnail": "img/easy_draft/products/base-atype/100/thumbnail/04.png",
                },
            ],
        },
        '230_435_310_1': {  # 100 wide
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
                    "image": "img/easy_draft/products/base-atype/100_wide/01.png",
                    "thumbnail": "img/easy_draft/products/base-atype/100_wide/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 534,
                                "y": 554,
                            },
                            "end": {  # bottom right
                                "x": 1126,
                                "y": 864,
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
                    "image": 'img/easy_draft/products/base-atype/100_wide/02.png',
                    "thumbnail": "img/easy_draft/products/base-atype/100_wide/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/base-atype/100_wide/03.png',
                    "thumbnail": "img/easy_draft/products/base-atype/100_wide/thumbnail/03.png",
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/base-atype/100_wide/04.png',
                    "thumbnail": "img/easy_draft/products/base-atype/100_wide/thumbnail/04.png",
                },
            ],
        },

        # 2 print areas
        '120_250_210_2': {  # 60
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
                    "image": "img/easy_draft/products/base-atype/60/01.png",
                    "thumbnail": "img/easy_draft/products/base-atype/60/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 532,
                                "y": 622,
                            },
                            "end": {  # bottom right
                                "x": 1124,
                                "y": 932,
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
                    "image": 'img/easy_draft/products/base-atype/60/02.png',
                    "thumbnail": "img/easy_draft/products/base-atype/60/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": True,
                    "image": 'img/easy_draft/products/base-atype/60/03.png',
                    "thumbnail": "img/easy_draft/products/base-atype/60/thumbnail/03.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 552,
                                "y": 642,
                            },
                            "end": {  # bottom right
                                "x": 1144,
                                "y": 952,
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
                    "image": 'img/easy_draft/products/base-atype/60/04.png',
                    "thumbnail": "img/easy_draft/products/base-atype/60/thumbnail/04.png",
                },
            ],
        },
        '190_250_190_2': {  # 60 wide
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
                    "image": "img/easy_draft/products/base-atype/60_wide/01.png",
                    "thumbnail": "img/easy_draft/products/base-atype/60_wide/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 532,
                                "y": 562,
                            },
                            "end": {  # bottom right
                                "x": 1124,
                                "y": 872,
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
                    "image": 'img/easy_draft/products/base-atype/60_wide/02.png',
                    "thumbnail": "img/easy_draft/products/base-atype/60_wide/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": True,
                    "image": 'img/easy_draft/products/base-atype/60_wide/03.png',
                    "thumbnail": "img/easy_draft/products/base-atype/60_wide/thumbnail/03.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 530,
                                "y": 562,
                            },
                            "end": {  # bottom right
                                "x": 1122,
                                "y": 872,
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
                    "image": 'img/easy_draft/products/base-atype/60_wide/04.png',
                    "thumbnail": "img/easy_draft/products/base-atype/60_wide/thumbnail/04.png",
                },
            ],
        },
        '150_310_220_2': {  # 80
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
                    "image": "img/easy_draft/products/base-atype/80/01.png",
                    "thumbnail": "img/easy_draft/products/base-atype/80/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 532,
                                "y": 600,
                            },
                            "end": {  # bottom right
                                "x": 1124,
                                "y": 910,
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
                    "image": 'img/easy_draft/products/base-atype/80/02.png',
                    "thumbnail": "img/easy_draft/products/base-atype/80/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": True,
                    "image": 'img/easy_draft/products/base-atype/80/03.png',
                    "thumbnail": "img/easy_draft/products/base-atype/80/thumbnail/03.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 532,
                                "y": 600,
                            },
                            "end": {  # bottom right
                                "x": 1124,
                                "y": 910,
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
                    "image": 'img/easy_draft/products/base-atype/80/04.png',
                    "thumbnail": "img/easy_draft/products/base-atype/80/thumbnail/04.png",
                },
            ],
        },
        '100_400_200_2': {  # 80 wide
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
                    "image": "img/easy_draft/products/base-atype/80_wide/01.png",
                    "thumbnail": "img/easy_draft/products/base-atype/80_wide/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 534,
                                "y": 748,
                            },
                            "end": {  # bottom right
                                "x": 1126,
                                "y": 996,
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
                    "image": 'img/easy_draft/products/base-atype/80_wide/02.png',
                    "thumbnail": "img/easy_draft/products/base-atype/80_wide/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": True,
                    "image": 'img/easy_draft/products/base-atype/80_wide/03.png',
                    "thumbnail": "img/easy_draft/products/base-atype/80_wide/thumbnail/03.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 534,
                                "y": 748,
                            },
                            "end": {  # bottom right
                                "x": 1126,
                                "y": 996,
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
                    "image": 'img/easy_draft/products/base-atype/80_wide/04.png',
                    "thumbnail": "img/easy_draft/products/base-atype/80_wide/thumbnail/04.png",
                },
            ],
        },
        '250_350_300_2': {  # 100
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
                    "image": "img/easy_draft/products/base-atype/100/01.png",
                    "thumbnail": "img/easy_draft/products/base-atype/100/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 532,
                                "y": 464,
                            },
                            "end": {  # bottom right
                                "x": 1124,
                                "y": 774,
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
                    "image": 'img/easy_draft/products/base-atype/100/02.png',
                    "thumbnail": "img/easy_draft/products/base-atype/100/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": True,
                    "image": 'img/easy_draft/products/base-atype/100/03.png',
                    "thumbnail": "img/easy_draft/products/base-atype/100/thumbnail/03.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 534,
                                "y": 748,
                            },
                            "end": {  # bottom right
                                "x": 1126,
                                "y": 996,
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
                    "image": 'img/easy_draft/products/base-atype/100/04.png',
                    "thumbnail": "img/easy_draft/products/base-atype/100/thumbnail/04.png",
                },
            ],
        },
        '230_435_310_2': {  # 100 wide
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
                    "image": "img/easy_draft/products/base-atype/100_wide/01.png",
                    "thumbnail": "img/easy_draft/products/base-atype/100_wide/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 534,
                                "y": 554,
                            },
                            "end": {  # bottom right
                                "x": 1126,
                                "y": 864,
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
                    "image": 'img/easy_draft/products/base-atype/100_wide/02.png',
                    "thumbnail": "img/easy_draft/products/base-atype/100_wide/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": True,
                    "image": 'img/easy_draft/products/base-atype/100_wide/03.png',
                    "thumbnail": "img/easy_draft/products/base-atype/100_wide/thumbnail/03.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 534,
                                "y": 554,
                            },
                            "end": {  # bottom right
                                "x": 1126,
                                "y": 864,
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
                    "image": 'img/easy_draft/products/base-atype/100_wide/04.png',
                    "thumbnail": "img/easy_draft/products/base-atype/100_wide/thumbnail/04.png",
                },
            ],
        },
    },
}


print(json.dumps(data, indent=2, ensure_ascii=False))
