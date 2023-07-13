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
        'value': 100,
        'extra': '',
        'image': '',
    },
    'max_ordering_quantity': {
        'name': '最大注文数',
        'value': 5000,
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
        'value': "フルカラー",
        'extra': '',
        'image': '',
    },
    'example': {
        'value': 106.8,
        'suffix': '円',
        'unit': '箱',
        'lot': 1000
    },
    'size_limit': {
        'height': {
            'min': 40,
            'max': 400,
        },
        'width': {
            'min': 30,
            'max': 300,
        },
        'depth': {
            'min': 30,
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
            "inside": None,
        },
        "surface_material": None,
        "surface_process": None,
        "emboss": None,
        "special_print": None,
        "bottom": None,
    },
    'option_order': [
        'color_num',
        'surface_material',
        'surface_process',
        'emboss',
        'special_print',
        'bottom',
        'print_area',
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
            '10': {'name': '1,000', 'value': 1000},
            '15': {'name': '1,500', 'value': 1500},
            '20': {'name': '2,000', 'value': 2000},
            '30': {'name': '3,000', 'value': 3000},
            '40': {'name': '4,000', 'value': 4000},
            '50': {'name': '5,000', 'value': 5000},
        },
    },
    'size': {
        'name': 'サイズ',
        'extra': 'サイズを選択してください',
        'required': True,
        'default': '1',
        'image': 'img/product_detail/paperbox/size/folding-carton/folding-carton_original.jpg',
        'widget_type': 'modal-radio',
        'options': {
            '1': {
                'name': '化粧品用内箱',
                'value': [
                    {'name': 'height', 'value': 150},
                    {'name': 'width', 'value': 40},
                    {'name': 'depth', 'value': 40},
                ],
                'extra': '高さ150mm 幅40mm 奥行き40mm',
                'image': 'img/product_detail/paperbox/size/folding-carton/folding-carton_cosmetics.jpg',
                'data': 'design_templates/paperbox/folding_carton/folding_carton_cosmetics.zip'
            },
            '2': {
                'name': ' 健康食品用内箱',
                'value': [
                    {'name': 'height', 'value': 160},
                    {'name': 'width', 'value': 80},
                    {'name': 'depth', 'value': 80},
                ],
                'extra': '高さ160mm 幅80mm 奥行き80mm',
                'image': 'img/product_detail/paperbox/size/folding-carton/folding-carton_foods.jpg',
                'data': 'design_templates/paperbox/folding_carton/folding_carton_foods.zip'
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
                    "title": "両面の印刷が可能です",
                    "layout_type": "vertical-list-lg",
                    "contents": [
                        {
                            "image": "img/product_detail/paperbox/print_area/folding-carton/print_area_01.jpg",
                        },
                        {
                            "image": "img/product_detail/paperbox/print_area/folding-carton/print_area_02.jpg",
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
                'image': 'img/product_detail/paperbox/expansion/folding-carton/outside.jpg',
                'widget_type': 'modal-check',
                'options': {
                    'A': {'name': 'A', 'value': 'A', 'extra': ''},
                    'B': {'name': 'B', 'value': 'B', 'extra': ''},
                    'C': {'name': 'C', 'value': 'C', 'extra': ''},
                    'D': {'name': 'D', 'value': 'D', 'extra': ''},
                    'E': {'name': 'E', 'value': 'E', 'extra': ''},
                    'F': {'name': 'F', 'value': 'F', 'extra': ''}
                },
            },
            'inside': {
                'name': '内側',
                'extra': '印刷面を選択してください',
                'required': True,
                'default': '',
                'image': 'img/product_detail/paperbox/expansion/folding-carton/inside.jpg',
                'widget_type': 'modal-check',
                'options': {
                    'A': {'name': 'A', 'value': 'A', 'extra': ''},
                    'B': {'name': 'B', 'value': 'B', 'extra': ''},
                    'C': {'name': 'C', 'value': 'C', 'extra': ''},
                    'D': {'name': 'D', 'value': 'D', 'extra': ''},
                    'E': {'name': 'E', 'value': 'E', 'extra': ''},
                    'F': {'name': 'F', 'value': 'F', 'extra': ''},
                    'G': {'name': 'G', 'value': 'G', 'extra': ''},
                    'H': {'name': 'H', 'value': 'H', 'extra': ''},
                    'I': {'name': 'I', 'value': 'I', 'extra': ''}
                }
            },
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
                            'image': 'img/product_detail/paperbox/expansion/folding-carton/outside.jpg',
                        },
                        {
                            'image': 'img/product_detail/paperbox/expansion/folding-carton/inside.jpg',
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
                'name': '普通 - カードB',
                'value': 'normal',
                'extra': '標準の生地です。特にこだわりがない場合はこの生地になります。。\n' \
                         '全体に色をプリントもでき、コストを抑えられますが、段目が見えるなど完成度は他と劣ります。',
                'image': 'img/product_detail/paperbox/surface_material/normal.jpg',
            },
            '2': {
                'name': '上質 - コートアイボリー',
                'value': 'ivory',
                'extra': '上質感を出せる生地です。コストは上がりますが選択可能です。',
                'image': 'img/product_detail/paperbox/surface_material/ivory.jpg'
            },
        },
        'note': {
            'title': '生地について',
            'sections': [
                {
                    'title': "２つから選択できます",
                    'layout_type': 'vertical-list-md',
                    'contents': [
                        {
                            'title': '普通 - カードB',
                            'image': 'img/product_detail/paperbox/surface_material/normal.jpg',
                            'body': [
                                '標準の生地です。特にこだわりがない場合はこの生地になります。',
                                '全体に色をプリントもでき、コストを抑えられますが、段目が見えるなど完成度は他と比べ劣ります。'
                            ]
                        },
                        {
                            'title': '上質 - コートアイボリー',
                            'image': 'img/product_detail/paperbox/surface_material/ivory.jpg',
                            'body': [
                                '上質感を出せる生地です。コストは上がりますが選択可能です。'
                            ]
                        },
                    ]
                }
            ]
        }
    },
    'surface_process': {
        'name': '加工',
        'extra': '',
        'required': False,
        'default': '1',
        'image': '',
        'widget_type': 'slider-lg',
        'options': {
            '1': {
                'name': '普通加工（OPニス）',
                'value': 'op',
                'extra': '標準の加工です。こだわりがない場合はこれがオススメです。',
                'image': 'img/product_detail/paperbox/surface_process/op.jpg'
            },
            '2': {
                'name': '上質加工（マットPP貼り）',
                'value': 'mattepp',
                'extra': 'ツルツルした触り心地に表面を加工でき、上質感が増します。',
                'image': 'img/product_detail/paperbox/surface_process/mattepp.jpg'
            },
        },
        'note': {
            'title': '加工について',
            'sections': [
                {
                    'title': "２つから選択できます",
                    'layout_type': 'vertical-list-sm',
                    'contents': [
                        {
                            'title': '普通加工（OPニス）',
                            'image': 'img/product_detail/paperbox/surface_process/op.jpg',
                            'body': [
                                '標準の加工です。こだわりがない場合はこれがオススメです。',
                            ]
                        },
                        {
                            'title': '上質加工（マットPP貼り）',
                            'image': 'img/product_detail/paperbox/surface_process/mattepp.jpg',
                            'body': [
                                'ツルツルした触り心地に表面を加工でき、上質感が増します。'
                            ]
                        },
                    ]
                }
            ]
        }
    },
    'bottom': {
        'name': '底の種類',
        'extra': '',
        'required': False,
        'default': '1',
        'image': '',
        'widget_type': 'slider-lg',
        'options': {
            '1': {
                'name': 'ワンタッチ底',
                'value': 'onetouch',
                'extra': '底２箇所を糊貼りして、自動的に底が形成されるタイプです。',
                'image': 'img/product_detail/paperbox/bottom/onetouch.jpg'
            },
            '2': {
                'name': 'キャラメル底',
                'value': 'caramel',
                'extra': '差し込み式で組み立てして底を形成するタイプです。',
                'image': 'img/product_detail/paperbox/bottom/caramel.jpg'
            },
        },
        'note': {
            'title': '底の種類について',
            'sections': [
                {
                    'title': "２つから選択できます",
                    'layout_type': 'horizontal-list-md',
                    'contents': [
                        {
                            'title': 'ワンタッチ底',
                            'image': 'img/product_detail/paperbox/bottom/onetouch.jpg',
                            'body': [
                                '底２箇所を糊貼りして、自動的に底が形成されるタイプです。',
                            ]
                        },
                        {
                            'title': 'キャラメル底',
                            'image': 'img/product_detail/paperbox/bottom/caramel.jpg',
                            'body': [
                                '差し込み式で組み立てして底を形成するタイプです。',
                            ]
                        },
                    ]
                }
            ]
        }
    },
    'emboss': {
        'name': '凹凸加工',
        'extra': '',
        'required': False,
        'default': '1',
        'image': '',
        'widget_type': 'slider-lg',
        'options': {
            '1': {
                'name': '追加しない',
                'value': 'none',
                'extra': '',
                'image': 'img/product_detail/common/no-style.jpg'
            },
            '2': {
                'name': 'エンボス - 凸加工',
                'value': 'emboss',
                'extra': '印刷部分が浮き出たせる加工です。',
                'image': 'img/product_detail/paperbox/emboss/emboss.jpg'
            },
            '3': {
                'name': 'デボス - 凹加工',
                'value': 'deboss',
                'extra': '印刷部分に窪みを付ける加工です。',
                'image':  'img/product_detail/paperbox/emboss/deboss.jpg'
            },
        },
        'note': {
            'title': '凹凸加工の追加について',
            'sections': [
                {
                    'title': "２つから選択できます",
                    'layout_type': 'horizontal-list-md',
                    'contents': [
                        {
                            'title': 'エンボス - 凸加工',
                            'image': 'img/product_detail/paperbox/emboss/emboss.jpg',
                            'body': [
                                '印刷部分が浮き出たせる加工です。',
                            ]
                        },
                        {
                            'title': 'デボス - 凹加工',
                            'image': 'img/product_detail/paperbox/emboss/deboss.jpg',
                            'body': [
                                '印刷部分に窪みを付ける加工です。',
                            ]
                        },
                    ]
                }
            ]
        }
    },
    'special_print': {
        'name': '特殊印刷',
        'extra': '',
        'required': False,
        'default': '1',
        'image': '',
        'widget_type': 'slider-lg',
        'options': {
            '1': {
                'name': '追加しない',
                'value': 'none',
                'extra': '',
                'image': 'img/product_detail/common/no-style.jpg'
            },
            '2': {
                'name': '箔押し - つや金',
                'value': 'gold',
                'extra': '金色のつやを出す追加加工です。',
                'image': 'img/product_detail/paperbox/special_print/gold.jpg'
            },
            '3': {
                'name': '箔押し - つや銀',
                'value': 'silver',
                'extra': '銀色のつやを出す追加加工です。',
                'image': 'img/product_detail/paperbox/special_print/silver.jpg'
            },
        },
        'note': {
            'title': '特殊印刷の追加について',
            'sections': [
                {
                    'title': "２つから選択できます",
                    'layout_type': 'horizontal-list-md',
                    'contents': [
                        {
                            'title': '箔押し - つや金',
                            'image': 'img/product_detail/paperbox/special_print/gold.jpg',
                            'body': [
                                '金色のつやを出す追加加工です。',
                            ]
                        },
                        {
                            'title': '箔押し - つや銀',
                            'image': 'img/product_detail/paperbox/special_print/silver.jpg',
                            'body': [
                                '銀色のつやを出す追加加工です。',
                            ]
                        },
                    ]
                }
            ]
        }
    },
}


print(json.dumps(data, indent=2, ensure_ascii=False))
