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
        'value': 100,
        'extra': '',
        'image': '',
    },
    'max_ordering_quantity': {
        'name': '最大注文数',
        'value': 2000,
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
            {'key': 'ジップ上の高さ', 'value': '32mm'},
            {'key': '基材構成', 'value': '表：PET#12//CP#50・裏：透明蒸着PET#12//VMPET#12//CP#50'},
            {'key': '加工', 'value': '底開き、吊り下げ穴付き、角丸加工、ノッチ付き'},
        ],
        'image': '',
    },
    'choosable_color': {
        'name': '印刷色',
        'value': "モノクロ1色",
        'extra': '',
        'image': '',
    },
    'example': {
        'value': 39.7,
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
        'default': '1',
        'image': '',
        'unit': '袋',
        'widget_type': 'radio',
        'options': {
            '1': {'name': '100', 'value': 100},
            '2': {'name': '200', 'value': 200},
            '3': {'name': '300', 'value': 300},
            '4': {'name': '400', 'value': 400},
            '5': {'name': '500', 'value': 500},
            '6': {'name': '600', 'value': 600},
            '7': {'name': '700', 'value': 700},
            '8': {'name': '800', 'value': 800},
            '9': {'name': '900', 'value': 900},
            '10': {'name': '1,000', 'value': 1000},
            '15': {'name': '1,500', 'value': 1500},
            '20': {'name': '2,000', 'value': 2000},
        },
    },
    'size': {
        'name': 'サイズ',
        'extra': 'サイズを選択してください',
        'required': True,
        'default': '1',
        'image': 'img/product_detail/film/size/zip-aluminum-clear-bag-small-lot/zip-aluminum-clear-bag_original.jpg',
        'widget_type': 'modal-radio',
        'options': {
            '1': {
                'name': 'アクセサリー',
                'value': [
                    {'name': 'height', 'value': 140},
                    {'name': 'width', 'value': 100},
                ],
                'extra': '高さ140mm 幅100mm',
                'image': 'img/product_detail/film/size/zip-aluminum-clear-bag-small-lot/zip-aluminum-clear-bag_accessories.jpg',
                'data': 'design_templates/flatbag/zip_aluminum_clear_bag_small_lot/zip_aluminum_clear_bag_accessories.ai'
            },
            '2': {
                'name': 'A6',
                'value': [
                    {'name': 'height', 'value': 170},
                    {'name': 'width', 'value': 120},
                ],
                'extra': '高さ170mm 幅120mm',
                'image': 'img/product_detail/film/size/zip-aluminum-clear-bag-small-lot/zip-aluminum-clear-bag_a6.jpg',
                'data': 'design_templates/flatbag/zip_aluminum_clear_bag_small_lot/zip_aluminum_clear_bag_a6.ai'
            },
            '3': {
                'name': 'B6',
                'value': [
                    {'name': 'height', 'value': 200},
                    {'name': 'width', 'value': 140},
                ],
                'extra': '高さ200mm 幅140mm',
                'image': 'img/product_detail/film/size/zip-aluminum-clear-bag-small-lot/zip-aluminum-clear-bag_b6.jpg',
                'data': 'design_templates/flatbag/zip_aluminum_clear_bag_small_lot/zip_aluminum_clear_bag_b6.ai'
            },
            '4': {
                'name': 'A5',
                'value': [
                    {'name': 'height', 'value': 240},
                    {'name': 'width', 'value': 170},
                ],
                'extra': '高さ240mm 幅170mm',
                'image': 'img/product_detail/film/size/zip-aluminum-clear-bag-small-lot/zip-aluminum-clear-bag_a5.jpg',
                'data': 'design_templates/flatbag/zip_aluminum_clear_bag_small_lot/zip_aluminum_clear_bag_a5.ai'
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
            }
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
        '200_140_1': {  # b6
            'pdf_size': {  # unit mm
                'height': 190,
                'width': 190,
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
                    "image": "img/easy_draft/products/zip-aluminum-clear-bag-small-lot/b6/01.png",
                    "thumbnail": "img/easy_draft/products/zip-aluminum-clear-bag-small-lot/b6/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 747,
                                "y": 385,
                            },
                            "end": {  # bottom right
                                "x": 963,
                                "y": 655,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 100,
                                "y": 120,
                            },
                        }
                    }
                },
                {
                    "name": "背面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/zip-aluminum-clear-bag-small-lot/b6/02.png',
                    "thumbnail": "img/easy_draft/products/zip-aluminum-clear-bag-small-lot/b6/thumbnail/02.png",
                },
            ],
        },
        '170_120_1': {  # a6
            'pdf_size': {  # unit mm
                'height': 140,
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
                    "image": "img/easy_draft/products/zip-aluminum-clear-bag-small-lot/a6/01.png",
                    "thumbnail": "img/easy_draft/products/zip-aluminum-clear-bag-small-lot/a6/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 788,
                                "y": 455,
                            },
                            "end": {  # bottom right
                                "x": 943,
                                "y": 610,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 70,
                                "y": 70,
                            },
                        }
                    }
                },
                {
                    "name": "背面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/zip-aluminum-clear-bag-small-lot/a6/02.png',
                    "thumbnail": "img/easy_draft/products/zip-aluminum-clear-bag-small-lot/a6/thumbnail/02.png",
                },
            ],
        },
        '140_100_1': {  # a5
            'pdf_size': {  # unit mm
                'height': 140,
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
                    "image": "img/easy_draft/products/zip-aluminum-clear-bag-small-lot/accessories/01.png",
                    "thumbnail": "img/easy_draft/products/zip-aluminum-clear-bag-small-lot/accessories/thumbnail/01.png",
                    "position": {
                        "image": {  # unit px
                            "start": {  # upper left
                                "x": 842,
                                "y": 445,
                            },
                            "end": {  # bottom right
                                "x": 984,
                                "y": 622,
                            },
                        },
                        "pdf": {  # unit mm
                            "start": {  # upper left
                                "x": 20,
                                "y": 20,
                            },
                            "end": {  # bottom right
                                "x": 60,
                                "y": 70,
                            },
                        }
                    }
                },
                {
                    "name": "背面",
                    "id": "B",
                    "is_printable": False,
                    "image": 'img/easy_draft/products/zip-aluminum-clear-bag-small-lot/accessories/02.png',
                    "thumbnail": "img/easy_draft/products/zip-aluminum-clear-bag-small-lot/accessories/thumbnail/02.png",
                },
            ],
        },
    }
}


print(json.dumps(data, indent=2, ensure_ascii=False))
