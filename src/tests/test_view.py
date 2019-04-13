from django.test import RequestFactory
from django.urls import reverse
from mixer.backend.django import mixer
import pytest
from main.views import Platform, ArticleView

@pytest.mark.django_db
class TestView:

    def test_platform(self):
        path = reverse('platform')
        request = RequestFactory().get(path)
        response = Platform.get(self, request)
        assert response.status_code == 200

