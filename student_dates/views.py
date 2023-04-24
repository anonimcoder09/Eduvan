from .serializers import StudentDatesSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import StudentDates

class StudentDatesVeiw(ListCreateAPIView):
    queryset = StudentDates.objects.all()
    serializer_class = StudentDatesSerializer

class StudentDatesDetail(RetrieveUpdateDestroyAPIView):
    queryset = StudentDates.objects.all()
    serializer_class = StudentDatesSerializer