__author__ = 'lorgio'
from rest_framework import serializers
from .models import User, Post, Photo

class UserSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedIdentityField(view_name='userpost-list', lookup_field='username')

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts',)

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    photos = serializers.HyperlinkedIdentityField(view_name='postphoto-list')
    # author = serializers.HyperlinkedRelatedField(view_name='user-detail', lookup_field='username')

    def get_validation_exclusions(self):
        # Se necesita excluir 'author'
        exclusions = super(PostSerializer, self).get_validation_exclusions()
        return exclusions + ['author']

    class Meta:
        model = Post

class PhotoSerializer(serializers.ModelSerializer):
    image = serializers.Field(default='image.url')

    class Meta:
        model = Photo