from allauth.account.models import EmailAddress
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class ColorMeAccount(ProviderAccount):
    pass


class ColorMeProvider(OAuth2Provider):

    id = 'colorme'
    name = 'Color Me'
    account_class = ColorMeAccount

    def extract_uid(self, data):
        return str(data['shop']['id'])

    def extract_common_fields(self, data):
        return dict(email=data['shop']['user_mail'],
                    name=data['shop']['name1'] + data['shop']['name2'],
                    company_name=data['shop']['title'],
                    url=data['shop']['url'])

    def extract_email_addresses(self, data):
        ret = []
        email = data['shop']['user_mail']
        if email and data.get('verified_email'):
            ret.append(EmailAddress(email=email,
                       verified=True,
                       primary=True))
        return ret


class BaseAccount(ProviderAccount):
    pass


class BaseProvider(OAuth2Provider):
    id = 'base'
    name = 'Base'
    account_class = BaseAccount

    def extract_uid(self, data):
        return str(data['user']['shop_id'])

    def extract_common_fields(self, data):
        return dict(email=data['user']['mail_address'],
                    name="担当者",
                    company_name=data['user']['shop_name'],
                    url=data['user']['shop_url'])

    def extract_email_addresses(self, data):
        ret = []
        email = data['user']['mail_address']
        if email and data.get('verified_email'):
            ret.append(EmailAddress(email=email,
                                    verified=True,
                                    primary=True))
        return ret

    def get_default_scope(self):
        return ['read_users_mail', ]


provider_classes = [ColorMeProvider, BaseProvider]
