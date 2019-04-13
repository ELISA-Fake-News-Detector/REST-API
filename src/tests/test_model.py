from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestModels:

    def test_platform_create_object(self):
        article = mixer.blend('main.Platform_Model')
        assert article.clean == None
