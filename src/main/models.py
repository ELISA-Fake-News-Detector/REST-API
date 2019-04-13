from django.db import models
from .choices import SOCIAL_MEDIA, SUBJECT
# Create your models here.


class Platform_Model(models.Model):
    """
    three fields are readonly and can be altered from django admin panel
    """
    hadoop_url = models.CharField(max_length=100)
    jupyter_url = models.CharField(max_length=100)
    colab_url = models.CharField(max_length=100)

    def __str__(self):
        return "Platform URLs"

    @property
    def clean(self):
        """
        Throw ValidationError if you try to save more than one model instance
        """
        model = self.__class__
        if (model.objects.count() > 0 and self.id != model.objects.get().id):
            raise ValidationError("Can only create 1 instance of %s." % model.__name__)


class Articles_Model(models.Model):
    """
    database fields with headline and content for fake news detection
    """
    headline = models.CharField(max_length=200)
    content = models.CharField(max_length=5000)

    def __str__(self):
        """
        to save first five characters as object name in admin panel
        """
        return str(headline[:5])


class Post_Model(models.Model):
    """
    post model 
    """
    post = models.CharField(max_length=30)
    social_media = models.CharField(choices=SOCIAL_MEDIA, default="Facebook", max_length=20)

    def __str__(self):
        return str(post[:30])

class Feedback_Model(models.Model):
    """
    feedback model 
    """
    expression = models.CharField(max_length=25)
    subject = models.CharField(choices=SUBJECT, max_length=500)
    message = models.CharField(max_length=1000)
    source = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(message[:30])


class URLModel(models.Model):
    """
    URL to headline, content -> reliability score
    """
    url = models.URLField()


class NewsAPIModel(models.Model):
    """
    get news from reliable sources from text
    """
    sentence = models.URLField()