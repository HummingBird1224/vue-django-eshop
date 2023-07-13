from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import BillingAddress, DeliveryAddress


User = get_user_model()


class UserModelTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="example@example.com",
            company_name="test inc.",
            name="first last",
            password="testpass",
        )
        self.user2 = User.objects.create_user(
            email="example2@example.com",
            company_name=None,
            name="first last",
            password="testpass",
        )
        self.auth_user = User.objects.create_superuser(
            email="auth@example.com",
            company_name="auth inc.",
            name="auth last",
            password="testpass",
        )
        self.billing = BillingAddress.objects.create(
            user=self.user,
            name="billing test",
            postal_code="100-0001",
            prefecture="tokyo",
            city="千代田区",
            building="皇居",
            tel="080-0000-0000",
            is_default=True,
        )
        self.billing2 = BillingAddress.objects.create(
            user=self.user,
            name="billing2 test",
            postal_code="064-8537",
            prefecture="北海道",
            city="札幌市中央区宮の森3条7丁目70番",
            tel="080-0000-0000",
        )
        self.delivery = DeliveryAddress.objects.create(
            user=self.user,
            name="billing test",
            postal_code="100-0001",
            prefecture="tokyo",
            city="千代田区",
            building="皇居",
            tel="080-0000-0000",
            is_default=True,
        )
        self.delivery2 = DeliveryAddress.objects.create(
            user=self.user,
            name="billing2 test",
            postal_code="064-8537",
            prefecture="北海道",
            city="札幌市中央区宮の森3条7丁目70番",
            tel="080-0000-0000",
        )

    def test_create_user(self):
        self.assertEqual(self.user.pk, self.user.id)
        self.assertEqual(self.auth_user.pk, self.auth_user.id)

        self.assertEqual(self.user.get_fullname(), "test inc. first last")
        self.assertEqual(self.user2.get_fullname(), "first last")

        self.assertTrue(self.user.has_payjp_customer())
        self.assertTrue(self.user.has_payjp_customer_id())

        self.assertFalse(self.user.is_staff)
        self.assertTrue(self.auth_user.is_staff)

    def test_address(self):
        self.assertEqual(self.user.get_default_billing_address(), self.billing)
        self.assertEqual(self.user.get_default_delivery_address(), self.delivery)

        self.assertFalse(self.billing2.is_default)
        self.assertFalse(self.delivery2.is_default)

        self.assertEqual(self.billing.get_full_address(), "tokyo千代田区皇居")
        self.assertEqual(self.delivery.get_full_address(), "tokyo千代田区皇居")

        self.assertEqual(self.billing2.get_full_address(), "北海道札幌市中央区宮の森3条7丁目70番")
        self.assertEqual(self.delivery2.get_full_address(), "北海道札幌市中央区宮の森3条7丁目70番")

        self.user.change_default_billing_address(self.billing2)
        self.user.change_default_delivery_address(self.delivery2)

        self.assertEqual(self.user.get_default_billing_address(), self.billing2)
        self.assertEqual(self.user.get_default_delivery_address(), self.delivery2)

        self.assertFalse(self.billing.is_default)
        self.assertFalse(self.delivery.is_default)



