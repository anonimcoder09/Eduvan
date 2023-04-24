from .serializers import CenterSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Center

class CenterVeiw(ListCreateAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer

class CenterDetail(RetrieveUpdateDestroyAPIView):
    queryset = Center.objects.all()
    serializer_class = CenterSerializer