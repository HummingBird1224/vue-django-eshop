from .payjp_functions import (payjp_confirm_charge,
                              payjp_create_charge_with_customer_id,
                              payjp_cancel_charge)


def capture_from_order(order):
    """注文アイテムのデザインが全てconfirmされていたら決済のcaptureを更新する。
    """
    from billing.models import Transaction

    capture = True
    for item in order.get_order_items():
        # TODO: exclude cannceled item.
        if item.design.state != 'confirmed':
            capture = False
    if capture:
        t = Transaction.objects.filter(order=order).first()
        # クレジットの場合は決済の確定をする
        # 銀行振込は手動なのでこの関数は無効
        if t.type == 'credit_card':
            payjp_confirm_charge(t.token)
            order.state = 'charge_confirmed'
            order.save()
            t.is_captured = True
            t.save()


def remake_transaction(order):
    """orderから新しい決済を作成する
    """
    from billing.models import Transaction

    t = Transaction.objects.filter(order=order).first()

    if t.type == 'credit_card':
        c_id = t.user.payjpinfo.customer_id
        charge = payjp_create_charge_with_customer_id(c_id,
                                                    order.total,
                                                    order.ref_code,
                                                    t.card)
        # TRANSACTION CREATION
        Transaction.objects.create(
            user=order.user,
            token=charge["id"],
            order=order,
            amount=order.total,
            card=t.card,
            type=t.type,
        )
    elif t.type == 'bank_transfer':
        # TRANSACTION CREATION
        Transaction.objects.create(
            user=order.user,
            token=t.token,
            order=order,
            amount=order.total,
            card=t.card,
            type=t.type,
        )


def cancel_transaction(order):
    """決済のキャンセル
    内部ではPayJPを使って返金という扱い
    """
    from billing.models import Transaction

    t = Transaction.objects.filter(order=order).first()
    if t.type == 'credit_card':
        payjp_cancel_charge(t.token)


