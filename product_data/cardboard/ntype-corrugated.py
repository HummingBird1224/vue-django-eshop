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
            'first': 14,
            'repeat': 10
        },
        'extra': {
            'first': 'データ確定後2週間',
            'repeat': '約10日',
        },
        'image': '',
    },
    'can_select_original_size': {
        'name': 'オリジナルサイズ',
        'value': True,
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
        'extra': [],
        'image': '',
    },
    'choosable_color': {
        'name': '印刷色',
        'value': "フルカラー・制限あり",
        'extra': '',
        'image': '',
    },
    'example': {
        'value': 125.7,
        'suffix': '円',
        'unit': '箱',
        'lot': 100
    },
    'size_limit': {
        'height': {
            'min': 25,
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
        "print_area": {
            "outside": None,
        },
        "surface_material": None,
        "surface_process": None,
    },
    'option_order': [
        'color_num',
        'surface_material',
        'surface_process',
        'print_area',
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
            '5': {'name': '500', 'value': 500},
            '10': {'name': '1,000', 'value': 1000},
            '15': {'name': '1,500', 'value': 1500},
            '20': {'name': '2,000', 'value': 2000},
            '30': {'name': '3,000', 'value': 3000},
        },
    },
    'size': {
        'name': 'サイズ',
        'extra': 'サイズを選択してください',
        'required': True,
        'default': '1',
        'image': 'img/product_detail/cardboard/size/ntype-corrugated/ntype-corrugated_original.jpg',
        'widget_type': 'modal-radio',
        'options': {
            '1': {
                'name': 'サプリメントボトル用',
                'value': [
                    {'name': 'height', 'value': 80},
                    {'name': 'width', 'value': 220},
                    {'name': 'depth', 'value': 140},
                ],
                'extra': '高さ80mm 幅220mm 奥行き140mm',
                'image': 'img/product_detail/cardboard/size/ntype-corrugated/ntype-corrugated_supplement.jpg',
                'data': 'design_templates/cardboard/ntype_corrugated/ntype_corrugated_supplement.ai'
            },
            '2': {
                'name': 'アパレル用',
                'value': [
                    {'name': 'height', 'value': 40},
                    {'name': 'width', 'value': 260},
                    {'name': 'depth', 'value': 200},
                ],
                'extra': '高さ40mm 幅260mm 奥行き200mm',
                'image': 'img/product_detail/cardboard/size/ntype-corrugated/ntype-corrugated_apparel.jpg',
                'data': 'design_templates/cardboard/ntype_corrugated/ntype_corrugated_apparel.ai'
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
                'image': 'img/product_detail/cardboard/expansion/ntype-corrugated/outside.jpg',
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
            #     'image': 'img/product_detail/cardboard/expansion/ntype-corrugated/inside.jpg',
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
                            'image': 'img/product_detail/cardboard/expansion/ntype-corrugated/outside.jpg',
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
                'image': 'img/product_detail/cardboard/surface_material/ntype-corrugated/material_1.jpg'
            },
            '2': {
                'name': '白ダンボール',
                'value': 'white',
                'extra': 'コストを抑えて上質感を出せる素材です。\n' \
                         '印刷に使える色に制限があります。',
                'image': 'img/product_detail/cardboard/surface_material/ntype-corrugated/material_2.jpg'
            },
            '3': {
                'name': '合紙素材',
                'value': 'laminating',
                'extra': '上から紙を張り合わせることで綺麗なプリントを実現できる素材です。\n' \
                         'コストはかかりますが、最も自由に印刷ができます。\n' \
                         '写真など色数の多いものは合紙を使うことでプリントできます。',
                'image': 'img/product_detail/cardboard/surface_material/ntype-corrugated/material_3.jpg'
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
                        {
                            "title": "合紙",
                            'image': 'img/product_detail/cardboard/surface_material/ntype-corrugated/material_3.jpg',
                            "body": [
                                "コストを抑えて上質感を出せる素材です。",
                                "印刷に使える色に制限があります。",
                            ],
                            'after': {
                                "layout_type": "grid-list-md",
                                "summary": {
                                    "title": "※表面加工オプションが選べます",
                                    "body": [
                                        "特殊な加工のため、注文の際はお問い合わせ扱いになります。",
                                    ]
                                },
                                "contents": [
                                    {
                                        'title': 'マットニス',
                                        'image': 'img/product_detail/cardboard/surface_process/mattevarnish.jpg',
                                        'body': [
                                            '基本的に合紙はこの加工を使います',
                                        ],
                                    },
                                    {
                                        'title': 'マットPP',
                                        'image': 'img/product_detail/cardboard/surface_process/mattepp.jpg',
                                        'body': [
                                            '発光を抑えた高級感のある質感になります',
                                        ],
                                    },
                                ]
                            }
                        }
                    ]
                },
            ]
        }
    },
    'surface_process': {
        'name': '表面加工',
        'extra': '',
        'required': False,
        'default': '1',
        'image': '',
        'widget_type': 'slider-lg',
        "condition": {
            "key": "surface_material",
            "operator": "equal",
            "value": "laminating",
        },
        'options': {
            '1': {
                'name': '追加しない',
                'value': 'none',
                'extra': '',
                'image': 'img/product_detail/common/no-style.jpg'
            },
            '2': {
                'name': 'マットニス',
                'value': 'mattevarnish',
                'extra': '表面の発光を抑える加工です。',
                'image': 'img/product_detail/cardboard/surface_process/mattevarnish.jpg'
            },
            '3': {
                'name': 'マットPP',
                'value': 'mattepp',
                'extra': '表面の発光を抑える加工です。',
                'image': 'img/product_detail/cardboard/surface_process/mattepp.jpg'
            },
        },
    },
}


print(json.dumps(data, indent=2, ensure_ascii=False))
