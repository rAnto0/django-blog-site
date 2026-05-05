from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class UsersAuthTests(TestCase):
    fixtures = ["initial_data.json"]

    def test_fixture_users_exist(self):
        user_model = get_user_model()
        self.assertTrue(user_model.objects.filter(username="admin").exists())
        self.assertTrue(user_model.objects.filter(username="editor").exists())

    def test_login_with_fixture_user(self):
        response = self.client.post(
            reverse("users:login"),
            {"username": "admin", "password": "admin12345"},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context["user"].is_authenticated)

    def test_profile_requires_authentication(self):
        response = self.client.get(reverse("users:profile"))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("users:login"), response.url)
