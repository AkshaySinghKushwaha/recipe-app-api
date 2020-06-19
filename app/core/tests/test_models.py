from django.test import TestCase
from django.contrib.auth import get_user_model


class UserTest(TestCase):

    def test_user_model(self):
        """test user creation with email and password"""
        email = "test@example.com"
        password = "mypass123"
        user = get_user_model().objects.create_user(
            email=email, password=password)

        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalization(self):
        """Test the user email domain is normalize in lower case"""
        email = "test@EXAMPLE.COM"
        password = "mypass123"
        user = get_user_model().objects.create_user(
            email, password)

        self.assertEquals(user.email, "test@example.com")

    def test_new_user_invalid_email(self):
        """Test new user if invalid email then raise value error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "newpass123")

    def test_new_super_user_creation(self):
        """Test new superuser is created or not """
        user = get_user_model().objects.create_superuser(
                "test@example.com",
                "newpass123")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
