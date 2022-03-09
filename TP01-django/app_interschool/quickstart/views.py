from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from app_interschool.quickstart.models import Event
from rest_framework import viewsets
from rest_framework import permissions
from app_interschool.quickstart.serializers import UserSerializer, GroupSerializer, EventSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('email').order_by('username',)
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]




from url_filter.integrations.drf import DjangoFilterBackend

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['titre']