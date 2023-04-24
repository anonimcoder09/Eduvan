from rest_framework import serializers
from .models import StudentDates

class StudentDatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDates
        fields = ['id', 'user_id', 'is_there', 'date']