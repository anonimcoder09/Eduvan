from rest_framework import serializers
from .models import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'teacher_name', 'time_lesson', 'center_id', 'created_at']