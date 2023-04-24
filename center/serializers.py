from rest_framework import serializers
from .models import Center

class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = ['id', 'name', 'responsible_person', 'number', 'location', 'created_at']