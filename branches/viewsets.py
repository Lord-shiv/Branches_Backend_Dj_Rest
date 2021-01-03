from rest_framework import viewsets
from . import models
from . import serializers


class BrachViewset(viewsets.ModelViewSet):
    queryset = models.Branch.objects.all()
    serializer_class = serializers.BranchSerializer
