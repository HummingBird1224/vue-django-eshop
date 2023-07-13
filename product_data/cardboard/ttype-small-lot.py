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
            {'key': '加工', 'value': 'ロック付き'},
            {'key': '厚み', 'value': '1.5mm'},
            {'key': 'サイズ', 'value': '外寸表記です。'},
            {'key': '①横', 'value': '外寸より5mm小さい'},
            {'key': '②縦', 'value': '外寸より3mm小さい'},
            {'key': '③高さ', 'value': '外寸より4mm小さい'},
        ],
        'image': '',
    },
    'choosable_color': {
        'name': '印刷色',
        'value': "1色（白・黒・青・赤・緑）",
        'extra': '',
        'image': '',
    },
    'example': {
        'value': 60.7,
        'suffix': '円',
        'unit': '箱',
        'lot': 100
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
        'default': '05',
        'image': '',
        'unit': '箱',
        'widget_type': 'radio',
        'options': {
            '05': {'name': '50', 'value': 50},
            '1': {'name': '100', 'value': 100},
            '2': {'name': '200', 'value': 200},
            '3': {'name': '300', 'value': 300},
        },
    },
    'size': {
        'name': 'サイズ',
        'extra': 'サイズを選択してください',
        'required': True,
        'default': '1',
        'image': 'img/product_detail/cardboard/size/ttype-small-lot/ttype_original.jpg',
        'widget_type': 'modal-radio',
        'options': {
            '1': {
                'name': 'A5サイズ',
                'value': [
                    {'name': 'height', 'value': 25},
                    {'name': 'width', 'value': 235},
                    {'name': 'depth', 'value': 176},
                ],
                'extra': '高さ25mm 幅235mm 奥行き176mm',
                'image': 'img/product_detail/cardboard/size/ttype-small-lot/ttype_a5.jpg',
                'data': 'design_templates/cardboard/ttype_small_lot/ttype_a5.ai'
            },
            '2': {
                'name': 'A4小サイズ',
                'value': [
                    {'name': 'height', 'value': 25},
                    {'name': 'width', 'value': 310},
                    {'name': 'depth', 'value': 228},
                ],
                'extra': '高さ25mm 幅310mm 奥行き228mm',
                'image': 'img/product_detail/cardboard/size/ttype-small-lot/ttype_a4_small.jpg',
                'data': 'design_templates/cardboard/ttype_small_lot/ttype_a4_small.ai'
            },
            '3': {
                'name': 'A4サイズ',
                'value': [
                    {'name': 'height', 'value': 30},
                    {'name': 'width', 'value': 335},
                    {'name': 'depth', 'value': 248},
                ],
                'extra': '高さ30mm 幅335mm 奥行き248mm',
                'image': 'img/product_detail/cardboard/size/ttype-small-lot/ttype_a4.jpg',
                'data': 'design_templates/cardboard/ttype_small_lot/ttype_a4.ai'
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
    'print_area': {
        'name': '印刷する面の数',
        'extra': '',
        'required': True,
        'default': '',
        'image': '',
        'options': {
            'outside': {
                'name': '外側',
                'extra': '印刷面を選択してください',
                'required': True,
                'default': '',
                'widget_type': 'modal-check',
                'image': 'img/product_detail/cardboard/expansion/ttype/outside.jpg',
                'options': {
                    'A': {'name': 'A', 'value': 'A', 'extra': ''},
                    'B': {'name': 'B', 'value': 'B', 'extra': ''},
                    'C': {'name': 'C', 'value': 'C', 'extra': ''},
                    'D': {'name': 'D', 'value': 'D', 'extra': ''},
                    'E': {'name': 'E', 'value': 'E', 'extra': ''},
                    'F': {'name': 'F', 'value': 'F', 'extra': ''}
                },
            },
            # 'inside': {
            #     'name': '内側',
            #     'extra': '',
            #     'required': True,
            #     'default': '',
            #     'widget_type': 'modal-check',
            #     'image': 'img/product_detail/cardboard/expansion/ttype/inside.jpg',
            #     'options': {
            #         'A': {'name': 'A', 'value': 'A', 'extra': ''},
            #         'B': {'name': 'B', 'value': 'B', 'extra': ''},
            #         'C': {'name': 'C', 'value': 'C', 'extra': ''},
            #         'D': {'name': 'D', 'value': 'D', 'extra': ''},
            #         'E': {'name': 'E', 'value': 'E', 'extra': ''},
            #         'F': {'name': 'F', 'value': 'F', 'extra': ''}
            #     }
            # }
        },
        'note': {
            "title": "面数と値段について",
            "sections": [
                {
                    "title": "印刷する面数が増えるほど、料金は上がります",
                    "layout_type": "horizontal-list-lg",
                    "summary": {
                        "body": [
                            "着色する面数に従って料金が変化します。面数のイメージは画像をご覧ください。",
                            "※図のサイズはイメージです。",
                        ]
                    },
                    "contents": [
                        {
                            'image': 'img/product_detail/cardboard/expansion/ttype/outside.jpg',
                        },
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
                'name': '通常',
                'value': 'normal',
                'extra': 'ダンボールそのままの素材です。\n' \
                         'コストを抑えられますが、段目が見えるなど完成度は他と劣ります。\n' \
                         '印刷に使える色に制限があります。',
                'image': 'img/product_detail/cardboard/surface_material/ttype/material_1.jpg'
            },
        },
        'note': {
            "title": "ダンボールの生地について",
            "sections": [
                {
                    "title": "表面素材の選択",
                    "layout_type": "vertical-list-sm",
                    "contents": [
                        {
                            "title": "通常",
                            'image': 'img/product_detail/cardboard/surface_material/ntype-corrugated/material_1.jpg',
                            "body": [
                                "ダンボールそのままの通常素材です。",
                                "コストを抑えられますが、段目が見えるなど完成度は他を劣ります。",
                                "印刷に使える色には制限があります。"
                            ]
                        },
                        {
                            "title": "白ダンボール",
                            'image': 'img/product_detail/cardboard/surface_material/ntype-corrugated/material_2.jpg',
                            "body": [
                                "コストを抑えて上質感を出せる素材です。",
                                "印刷に使える色に制限があります。",
                            ]
                        },
                    ]
                },
            ]
        }
    },
    'zipper': {
        'name': 'ジッパー',
        'extra': '',
        'required': False,
        'default': '1',
        'image': '',
        'widget_type': 'slider-lg',
        'options': {
            '1': {
                'name': 'ジッパーなし',
                'value': False,
                'extra': '差し込みを使って開閉する形になります。',
                'image': 'img/product_detail/cardboard/process/zipper_false.png'
            },
            '2': {
                'name': 'ジッパーあり',
                'value': True,
                'extra': '切り取りで開閉できるジッパー付きです。',
                'image': 'img/product_detail/cardboard/process/zipper_true.png'
            }
        },
        'note': {
            "title": "ジッパーについて",
            "sections": [
                {
                    "title": "ジッパーの有無の選択",
                    "layout_type": "grid-list-md",
                    "contents": [
                        {
                            "title": "ジッパーなし",
                            'image': 'img/product_detail/cardboard/process/zipper_false.png',
                        },
                        {
                            "title": "ジッパーあり",
                            'image': 'img/product_detail/cardboard/process/zipper_true.png',
                        },
                    ]
                }
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
            '2': {
                'name': '２つ',
                'value': 2,
                'extra': '',
                'image': '',
                "condition": {
                    "key": "print_area_num",
                    "operator": "equal",
                    "value": 2,
                },
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
    # EASY DRAFT
    'easy_draft': {
        # height_width_depth
        '25_235_176_1': {  # a5
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
                    "image": "img/easy_draft/products/ttype-small-lot/a5/01.png",
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a5/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 538,
                                "y": 496,
                            },
                            "end": {  # bottom right
                                "x": 1126,
                                "y": 804,
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
                    "image": 'img/easy_draft/products/ttype-small-lot/a5/02.png',
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a5/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/ttype-small-lot/a5/03.png',
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a5/thumbnail/03.png",
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/ttype-small-lot/a5/04.png',
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a5/thumbnail/04.png",
                },
            ],
        },
        '25_310_228_1': {  # a4 small
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
                    "image": "img/easy_draft/products/ttype-small-lot/a4_small/01.png",
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a4_small/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 524,
                                "y": 466,
                            },
                            "end": {  # bottom right
                                "x": 1112,
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
                    "image": 'img/easy_draft/products/ttype-small-lot/a4_small/02.png',
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a4_small/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/ttype-small-lot/a4_small/03.png',
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a4_small/thumbnail/03.png",
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/ttype-small-lot/a4_small/04.png',
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a4_small/thumbnail/04.png",
                },
            ],
        },
        '30_335_248_1': {  # a4
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
                    "image": "img/easy_draft/products/ttype-small-lot/a4/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 556,
                                "y": 432,
                            },
                            "end": {  # bottom right
                                "x": 1144,
                                "y": 740,
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
                    "image": 'img/easy_draft/products/ttype-small-lot/a4/02.png',
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a4/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/ttype-small-lot/a4/03.png',
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a4/thumbnail/03.png",
                },
                {
                    "name": "右面",
                    "id": "D",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/ttype-small-lot/a4/04.png',
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a4/thumbnail/04.png",
                },
            ],
        },

        # 2 print areas
        '25_235_176_2': {  # a5
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
                    "image": "img/easy_draft/products/ttype-small-lot/a5/01.png",
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a5/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 538,
                                "y": 496,
                            },
                            "end": {  # bottom right
                                "x": 1126,
                                "y": 804,
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
                    "image": 'img/easy_draft/products/ttype-small-lot/a5/02.png',
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a5/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": True,
                    "image": 'img/easy_draft/products/ttype-small-lot/a5/03.png',
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a5/thumbnail/03.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 550,
                                "y": 496,
                            },
                            "end": {  # bottom right
                                "x": 1138,
                                "y": 804,
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
                    "image": 'img/easy_draft/products/ttype-small-lot/a5/04.png',
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a5/thumbnail/04.png",
                },
            ],
        },
        '25_310_228_2': {  # a4 small
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
                    "image": "img/easy_draft/products/ttype-small-lot/a4_small/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 524,
                                "y": 466,
                            },
                            "end": {  # bottom right
                                "x": 1112,
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
                    "image": 'img/easy_draft/products/ttype-small-lot/a4_small/02.png',
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a4_small/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": True,
                    "image": 'img/easy_draft/products/ttype-small-lot/a4_small/03.png',
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a4_small/thumbnail/03.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 554,
                                "y": 410,
                            },
                            "end": {  # bottom right
                                "x": 1142,
                                "y": 718,
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
                    "image": 'img/easy_draft/products/ttype-small-lot/a4_small/04.png',
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a4_small/thumbnail/04.png",
                },
            ],
        },
        '30_335_248_2': {  # a4
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
                    "image": "img/easy_draft/products/ttype-small-lot/a4/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 556,
                                "y": 432,
                            },
                            "end": {  # bottom right
                                "x": 1144,
                                "y": 740,
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
                    "image": 'img/easy_draft/products/ttype-small-lot/a4/02.png',
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a4/thumbnail/02.png",
                },
                {
                    "name": "背面",
                    "id": "C",
                    "is_printable": True,
                    "image": 'img/easy_draft/products/ttype-small-lot/a4/03.png',
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a4/thumbnail/03.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 556,
                                "y": 432,
                            },
                            "end": {  # bottom right
                                "x": 1144,
                                "y": 740,
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
                    "image": 'img/easy_draft/products/ttype-small-lot/a4/04.png',
                    "thumbnail": "img/easy_draft/products/ttype-small-lot/a4/thumbnail/04.png",
                },
            ],
        },
    },
}


print(json.dumps(data, indent=2, ensure_ascii=False))
