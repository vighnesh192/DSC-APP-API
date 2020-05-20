from users.models import Users
from rest_framework import viewsets, permissions
from .serializers import UsersSerializer

# ViewSets are similar to views
# which gets rendered with respect to a specific API call(GET, POST, etc.) 
class UsersViewSets(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UsersSerializer