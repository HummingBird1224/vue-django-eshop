from django.conf import settings
import payjp
import json


payjp.api_key = settings.PAYJP_API_KEY


def payjp_create_customer(description):
    """ create customer and return its id.
    """
    res = payjp.Customer.create(
        description=description
    )
    return res["id"]


def payjp_get_customer(customer_id):
    """
    """
    res = payjp.Customer.retrieve(customer_id)
    return json.loads(res)


def payjp_get_customer_cards(customer_id):
    """ get all (max 10) of the cards.
    """
    customer = payjp.Customer.retrieve(customer_id)
    cards = customer.cards.all()
    res = []
    for c in cards.data:
        res.append({
            "name": c.name,
            "id": c.id,
            "brand": c.brand,
            "last4": c.last4,
            "exp_month": c.exp_month,
            "exp_year": c.exp_year
        })
    return res


def payjp_get_card_info_with_customer_id(customer_id, card_id):
    """ get token(card) info from id.
    """
    customer = payjp.Customer.retrieve(customer_id)
    res = customer.cards.retrieve(card_id)
    return res


def payjp_get_card_info(charge_id):
    res = payjp.Charge.retrieve(charge_id)
    return res.card


def payjp_create_card(customer_id, token_id):
    """ create a card for given customer by assigning a token.
    """
    customer = payjp.Customer.retrieve(customer_id)
    res = customer.cards.create(
        card=token_id,
        default=True
    )
    return res["id"]


def payjp_delete_card(customer_id, card_id):
    """ delete a card from customer cards list.
    """
    customer = payjp.Customer.retrieve(customer_id)
    card = customer.cards.retrieve(card_id)
    card.delete()


def payjp_change_default_card(customer_id, card_id):
    """ change default card object of the customer
    """
    customer = payjp.Customer.retrieve(customer_id)
    customer.default_card = card_id
    customer.save()


def payjp_has_card(customer_id, token):
    res = payjp.Token.retrieve(token)
    cards = payjp_get_customer_cards(customer_id)
    for card in cards:
        if card['brand'] == res.card.brand and \
            card['exp_year'] == res.card.exp_year and \
            card['exp_month'] == res.card.exp_month and \
            card['last4'] == res.card.last4:
            return card['id']
    return None


def payjp_create_charge_with_customer_id(customer_id, amount, ref_code, card_id=None):
    """ create charge. charge will be made by customer's default card.
    WARN: THIS IS CRUCIAL.
    NOTE: amount must be 50~9,999,999.
    """
    # IF USING SPECIFIC CARD
    if card_id:
        res = payjp.Charge.create(
            amount=amount,
            customer=customer_id,
            card=card_id,
            description=ref_code,
            currency='jpy',
            capture=False,
            expiry_days=settings.PAYJP_EXPIRY_DAYS
        )
    # USING DEFAULT CARD
    else:
        res = payjp.Charge.create(
            amount=amount,
            customer=customer_id,
            description=ref_code,
            currency='jpy',
            capture=False,
            expiry_days=settings.PAYJP_EXPIRY_DAYS
        )
    return res


def payjp_create_charge(amount, ref_code, token):
    res = payjp.Charge.create(
        amount=amount,
        description=ref_code,
        card=token,
        currency='jpy',
        capture=False,
        expiry_days=settings.PAYJP_EXPIRY_DAYS
    )
    return res


def payjp_confirm_charge(charge_id):
    charge = payjp.Charge.retrieve(charge_id)
    res = charge.capture()
    return res


def payjp_get_default_card(customer_id):
    """ return info about default card.
    """
    customer = payjp.Customer.retrieve(customer_id)
    return customer.default_card


def payjp_cancel_charge(charge_id):
    charge = payjp.Charge.retrieve(charge_id)
    res = charge.refund()
    return res
