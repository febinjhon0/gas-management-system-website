from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class LoginTests(TestCase):
    def test_login_without_group_redirects_to_user_panel(self):
        User.objects.create_user(
            username='tester@example.com',
            email='tester@example.com',
            password='secret123',
        )

        response = self.client.post(reverse('login_post'), {
            'email': 'tester@example.com',
            'paswd': 'secret123',
        })

        self.assertRedirects(response, reverse('user'))
