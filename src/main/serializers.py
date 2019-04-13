from django.db.models import Q # for queries
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Platform_Model, Articles_Model, Post_Model, Feedback_Model, URLModel, NewsAPIModel
from django.core.exceptions import ValidationError
from .choices import SOCIAL_MEDIA, SUBJECT

class PlatformSerializer(serializers.ModelSerializer):
    """
    serializer having platform url to save in database
    fields are readonly and can be altered using djang admin panel only at localhost/admin
    """
    hadoop_url = serializers.CharField(read_only=True)
    jupyter_url = serializers.CharField(read_only=True)
    colab_url = serializers.CharField(read_only=True)

    class Meta:
        model = Platform_Model
        fields = (
            'hadoop_url',
            'jupyter_url',
            'colab_url'
        )
        read_only_fields = (
            'hadoop_url',
            'jupyter_url',
            'colab_url'
        )


class ArticlesSerializer(serializers.ModelSerializer):
    """
    serializer class to show fields in REST API call
    two fields with POST option
    return will show analyis data in the form of JSON object
    """

    headline = serializers.CharField(max_length=200)
    content = serializers.CharField(max_length=5000)

    class Meta:
        model = Articles_Model
        fields = (
            'headline',
            'content',
        )


class PostSerializer(serializers.ModelSerializer):
    """
    SERIALIZER for social media fake news detection
    serializer class to show fields in REST API call
    two fields with POST option having choices
    return will show analyis data in the form of JSON object
    """
    post = serializers.CharField(max_length=30)
    social_media =  serializers.ChoiceField(choices=SOCIAL_MEDIA)

    class Meta:
        model = Post_Model
        fields = (
            'post',
            'social_media',
        )

class FeedbackSerializer(serializers.ModelSerializer):
    """
    Serializer for saving user feedback based on different subject
    """

    expression = serializers.CharField(max_length=25)
    subject = serializers.ChoiceField(choices=SUBJECT)
    message = serializers.CharField(max_length=1000)
    source = serializers.CharField(max_length=500, allow_blank=True)

    class Meta:
        model = Feedback_Model
        fields = (
            'expression',
            'subject',
            'message',
            'source'
        )


class URLSerializer(serializers.ModelSerializer):
    """
    convert url to news article and predict reliability score
    """

    url = serializers.URLField(max_length=500)

    class Meta:
        model = URLModel
        fields = '__all__'

class NewsAPISerializer(serializers.ModelSerializer):
    """
    fetch news from text
    """

    sentence = serializers.CharField(max_length=1000)
    class Meta:
        model = NewsAPIModel
        fields = '__all__'