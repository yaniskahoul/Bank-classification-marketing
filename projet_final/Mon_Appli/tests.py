from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class SimpleTest(TestCase):
    def setUp(self):
        # Setup run before every test method.
        self.client = Client()
        self.home_url = reverse('home')
        self.login_url = reverse('login')

    def test_home_view(self):
        # Test the home view
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_user_login_GET(self):
        # Test login page access
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertIsInstance(response.context['form'], AuthenticationForm)

    def test_user_login_POST_valid(self):
        # Create a user for authentication
        User.objects.create_user('testuser', 'test@example.com', 'testpassword')
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302)  # expecting a redirect to home
        self.assertTrue(response.url.startswith(self.home_url))

    def test_user_login_POST_invalid(self):
        # Test invalid login attempt
        response = self.client.post(self.login_url, {
            'username': 'wronguser',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')
        self.assertFalse(response.context['form'].is_valid())