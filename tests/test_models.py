from rest_framework.test import APITestCase
from authentication.models import User

# During the following test, the username, 'meso' served as the superuser for security purposes, it has been changed
class TestModel(APITestCase):

    def test_creates_user(self):
        user = User.objects.create_user('meso', 'meso@company.com', 'meso123')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'meso@company.com')

    def test_creates_super_user(self):
        user = User.objects.create_superuser('meso', 'meso@company.com', 'meso123')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'meso@company.com')

    def test_raises_error_when_no_username_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='', email='meso@company.com', password='meso123')

    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user, username='username', email='',
                          password='meso123')

    def test_creates_user_with_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username='meso', email='meso@company.com', password='meso123', is_staff=False)

    def test_creates_user_with_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='meso', email='meso@company.com', password='meso123',
                                          is_superuser=False)
