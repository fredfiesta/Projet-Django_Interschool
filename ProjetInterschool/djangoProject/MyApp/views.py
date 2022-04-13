from django.shortcuts import render
from rest_framework import viewsets,filters, permissions,generics
from django.contrib.auth.models import User, Group
from django_filters.rest_framework import DjangoFilterBackend as NewFilter
from url_filter.integrations.drf import DjangoFilterBackend

from .serializers import *
from . import models

"""filter_backends = [DjangoFilterBackend,NewFilter,filters.SearchFilter,filters.OrderingFilter]
    filter_fields = '__all__'
    search_fields = '__all__'
    ordering_fields = '__all__'
    """

class EventViewSet(viewsets.ModelViewSet):
    queryset=models.Event.objects.all()
    serializer_class=EventSerializers


class LieuViewSet(viewsets.ModelViewSet):
    queryset=models.Lieu.objects.all()
    serializer_class=LieuSerializers

class CommentaireViewSet(viewsets.ModelViewSet):
    queryset=models.Commentaire.objects.all()
    serializer_class=CommentaireSerializers

class CommentaireLieuViewSet(viewsets.ModelViewSet):
    queryset=models.CommentaireLieu.objects.all()
    serializer_class=CommentaireLieuSerializers

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
