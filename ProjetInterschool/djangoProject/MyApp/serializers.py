from . import models
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class EventSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=models.Event
        fields='__all__' # ce qui yaura sur la vue


class LieuSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=models.Lieu
        fields='__all__'

class CommentaireSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=models.Commentaire
        fields='__all__'

class CommentaireLieuSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=models.Commentaire
        fields='__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']