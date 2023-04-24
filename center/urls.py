from django.urls import path
from .views import CenterVeiw, CenterDetail

urlpatterns = [
    path('', CenterVeiw.as_view()),
    path('<int:pk>/', CenterDetail.as_view()),
]