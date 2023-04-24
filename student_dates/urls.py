from django.urls import path
from .views import StudentDatesVeiw, StudentDatesDetail

urlpatterns = [
    path('', StudentDatesVeiw.as_view()),
    path('<int:pk>/', StudentDatesDetail.as_view()),
]