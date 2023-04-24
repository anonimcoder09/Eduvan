from django.urls import path
from .views import StudentVeiw, StudentDetail

urlpatterns = [
    path('', StudentVeiw.as_view()),
    path('<int:pk>/', StudentDetail.as_view()),
]