from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTest(TestCase):
    def test_create_user_with_email(self):
        email = "test@test.com"
        password = "test"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = "test@TEST.com"
        user = get_user_model().objects.create_user(email, "pass123")

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None,"pass123"
            )

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            "testsuper@test.com",
            "pass123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

