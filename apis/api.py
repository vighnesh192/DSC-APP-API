from apis.models import Apis
from rest_framework import viewsets, permissions
from .serializers import ApisSerializer

# ViewSets are similar to views
# which gets rendered with respect to a specific API call(GET, POST, etc.) 
class ApisViewSets(viewsets.ModelViewSet):
    queryset = Apis.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ApisSerializer