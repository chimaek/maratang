from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from quick.serializers import UserSerializer, GroupSerializer
from django.http import JsonResponse


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

def health(request):
    return JsonResponse({"status": "UP"}, status=200)
