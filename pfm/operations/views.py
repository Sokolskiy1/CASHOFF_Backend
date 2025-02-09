from rest_framework import viewsets
from .models import Operation
from .serializers import OperationSerializer

class OperationViewSet(viewsets.ModelViewSet):
    queryset = Operation.objects.all()
    serializer_class = OperationSerializer