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
        'value': 500,
        'extra': '',
        'image': '',
    },
    'estimated_shipping_date': {
        'name': '納期',
        'value': {
            'first': 7,
            'repeat': 7
        },
        'extra': {
            'first': 'データ確定後1週間',
            'repeat': 'データ確定後1週間',
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
            {'key': '厚み', 'value': '60サイズと80サイズは3mm、100サイズは5mm'},
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
        'value': 230,
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
        "surface_material": None,
    },
    'option_order': [
        'color_num',
        'surface_material',
        'size',
        'quantity'
    ],
    'quantity': {
        'name': '注文数',
        'extra': '',
        'required': True,
        'default': '1',
        'image': '',
        'unit': '箱',
        'widget_type': 'radio',
        'options': {
            '1': {'name': '100', 'value': 100},
            '2': {'name': '200', 'value': 200},
            '3': {'name': '300', 'value': 300},
            '4': {'name': '400', 'value': 400},
            '5': {'name': '500', 'value': 500},
        },
    },
    'size': {
        'name': 'サイズ',
        'extra': 'サイズを選択してください',
        'required': True,
        'default': '1',
        'image': 'img/product_detail/cardboard/size/ntype-corrugated-small-lot/ntype-corrugated_original.jpg',
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
                'image': 'img/product_detail/cardboard/size/atype-small-lot/atype_60.jpg',
                'data': 'design_templates/cardboard/atype_small_lot/atype_60.ai'
            },
            '2': {
                'name': '80サイズ',
                'value': [
                    {'name': 'height', 'value': 150},
                    {'name': 'width', 'value': 310},
                    {'name': 'depth', 'value': 220},
                ],
                'extra': '高さ150mm 幅310mm 奥行き220mm',
                'image': 'img/product_detail/cardboard/size/atype-small-lot/atype_80.jpg',
                'data': 'design_templates/cardboard/atype_small_lot/atype_80.ai'
            },
            '3': {
                'name': '100サイズ',
                'value': [
                    {'name': 'height', 'value': 250},
                    {'name': 'width', 'value': 350},
                    {'name': 'depth', 'value': 300},
                ],
                'extra': '高さ250mm 幅350mm 奥行き300mm',
                'image': 'img/product_detail/cardboard/size/atype-small-lot/atype_100.jpg',
                'data': 'design_templates/cardboard/atype_small_lot/atype_100.ai'
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
        'name': '材質',
        'extra': '',
        'required': True,
        'default': '1',
        'image': '',
        'widget_type': 'slider-lg',
        'options': {
            '1': {
                'name': '両面クラフト',
                'value': 'both_side_craft',
                'extra': '',
                'image': 'img/product_detail/cardboard/surface_material/atype/both_side_craft.jpg'
            },
            '2': {
                'name': '片面白片面クラフト',
                'value': 'single_side_craft',
                'extra': '',
                'image': 'img/product_detail/cardboard/surface_material/atype/single_side_craft.jpg',
            },
        },
    }
}


print(json.dumps(data, indent=2, ensure_ascii=False))
