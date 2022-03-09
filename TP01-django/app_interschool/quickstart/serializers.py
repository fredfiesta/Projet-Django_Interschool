from django.contrib.auth.models import User, Group
from app_interschool.quickstart.models import Evenement
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EvenementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evenement
        fields = ['date_creation', 'date',
                  'titre', 'lieu', 'lieu', 'desc']
