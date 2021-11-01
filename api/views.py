from django.db.models import query
from rest_framework import generics, serializers
from django.contrib.auth.models import User
from .serializers import UserDetailedSerializer


class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailedSerializer
