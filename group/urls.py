from django.urls import path
from .views import GroupVeiw, GroupDetail

urlpatterns = [
    path('', GroupVeiw.as_view()),
    path('<int:pk>/', GroupDetail.as_view()),
]