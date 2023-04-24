from django.urls import path
from .views import UserVeiw, UserDetail

urlpatterns = [
    path('', UserVeiw.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
]