from django.urls import reverse, resolve
from django.test import TestCase

class TestUrls(TestCase):

    def test_index_url(self):
        path = reverse('index')
        assert resolve(path).view_name == 'index'

    def test_api_url(self):
        path = reverse('api')
        assert resolve(path).view_name == 'api'

    def test_platform_url(self):
        path = reverse('platform')
        assert resolve(path).view_name == 'platform'

    def test_article_url(self):
        path = reverse('article')
        assert resolve(path).view_name == 'article'

    def test_post_url(self):
        path = reverse('post')
        assert resolve(path).view_name == 'post'
