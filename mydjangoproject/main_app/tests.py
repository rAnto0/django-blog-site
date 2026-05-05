from django.test import TestCase
from django.urls import reverse

from main_app.models import Category, Posts, TagPost


class MainAppViewsTests(TestCase):
    fixtures = ["initial_data.json"]

    def test_fixture_loaded_core_entities(self):
        self.assertEqual(Posts.objects.count(), 4)
        self.assertEqual(Posts.published.count(), 3)
        self.assertEqual(Category.objects.count(), 3)
        self.assertEqual(TagPost.objects.count(), 4)

    def test_main_page_shows_only_published_posts(self):
        response = self.client.get(reverse("main"))

        self.assertEqual(response.status_code, 200)
        posts = list(response.context["posts"])
        self.assertEqual(len(posts), 3)
        self.assertTrue(all(post.is_published for post in posts))

    def test_post_detail_for_draft_returns_404(self):
        response = self.client.get(reverse("post", kwargs={"post_slug": "draft-ui-improvements-ideas"}))
        self.assertEqual(response.status_code, 404)

    def test_category_and_tag_pages_are_available(self):
        category_response = self.client.get(reverse("category", kwargs={"cat_slug": "django"}))
        tag_response = self.client.get(reverse("tag", kwargs={"tag_slug": "best-practices"}))

        self.assertEqual(category_response.status_code, 200)
        self.assertEqual(tag_response.status_code, 200)
