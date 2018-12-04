from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView

from . import serializers

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer