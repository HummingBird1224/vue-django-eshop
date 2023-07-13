import json

data = {
    'contact_required': {
        'name': 'お問い合わせ',
        'value': False,
        'extra': '',
        'image': '',
    },
    'sample_order': {
        'name': 'サンプル注文',
        'value': True,
        'extra': '',
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
        'value': 200,
        'extra': '',
        'image': '',
    },
    'max_ordering_quantity': {
        'name': '最大注文数',
        'value': 1000,
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
            {'key': "材質", 'value': "未晒クラフト80g/㎡"},
            {'key': "持ち手", 'value': "紙ひもねじれ"},
            {'key': "表面加工", 'value': "なし"},
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
            'min': 1,
            'max': 600,
        },
        'width': {
            'min': 1,
            'max': 600,
        },
        'depth': {
            'min': 1,
            'max': 600,
        }
    },
    'shipping_area': {
        'exclude': True,
        'prefectures': [
            '沖縄',
            '北海道',
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
        'default': '20',
        'image': '',
        'unit': '袋',
        'widget_type': 'radio',
        'options': {
            '20': {'name': '200', 'value': 200},
            '40': {'name': '400', 'value': 400},
            '60': {'name': '600', 'value': 600},
            '80': {'name': '800', 'value': 800},
            '100': {'name': '1,000', 'value': 1000},
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
                'name': 'A5マチ広',
                'value': [
                    {'name': 'height', 'value': 210},
                    {'name': 'width', 'value': 180},
                    {'name': 'depth', 'value': 100},
                ],
                'extra': '高さ210mm 幅180mm マチ100mm',
                'image': 'img/external/base/size/handle-white-paperbag/a5_deep.jpg',
                'data': ''
            },
            '2': {
                'name': 'B5マチ広',
                'value': [
                    {'name': 'height', 'value': 250},
                    {'name': 'width', 'value': 200},
                    {'name': 'depth', 'value': 120},
                ],
                'extra': '高さ250mm 幅200mm マチ120mm',
                'image': 'img/external/base/size/handle-white-paperbag/b5_deep.jpg',
                'data': ''
            },
            '3': {
                'name': 'A5正方形',
                'value': [
                    {'name': 'height', 'value': 230},
                    {'name': 'width', 'value': 220},
                    {'name': 'depth', 'value': 60},
                ],
                'extra': '高さ230mm 幅220mm マチ60mm',
                'image': 'img/external/base/size/handle-white-paperbag/a5_square.jpg',
                'data': ''
            },
            '4': {
                'name': 'A4マチ広',
                'value': [
                    {'name': 'height', 'value': 300},
                    {'name': 'width', 'value': 220},
                    {'name': 'depth', 'value': 100},
                ],
                'extra': '高さ300mm 幅220mm マチ100mm',
                'image': 'img/external/base/size/handle-white-paperbag/a4_deep.jpg',
                'data': ''
            },
            '5': {
                'name': 'A4幅大',
                'value': [
                    {'name': 'height', 'value': 310},
                    {'name': 'width', 'value': 260},
                    {'name': 'depth', 'value': 60},
                ],
                'extra': '高さ310mm 幅260mm マチ60mm',
                'image': 'img/external/base/size/handle-white-paperbag/a4_wide.jpg',
                'data': ''
            },
            '6': {
                'name': 'A4幅大マチ広',
                'value': [
                    {'name': 'height', 'value': 330},
                    {'name': 'width', 'value': 260},
                    {'name': 'depth', 'value': 110},
                ],
                'extra': '高さ330mm 幅260mm マチ110mm',
                'image': 'img/external/base/size/handle-white-paperbag/a4_wide_deep.jpg',
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
    'choosable_color': [
        {'name': '白', 'image': 'img/external/base/color/white.png'},
        {'name': '黒', 'image': 'img/external/base/color/black.png'},
        {'name': '金', 'image': 'img/external/base/color/gold.png'},
        {'name': '銀', 'image': 'img/external/base/color/silver.png'},
    ],
}


print(json.dumps(data, indent=2, ensure_ascii=False))
