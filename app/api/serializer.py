from rest_framework import serializers
from webapp.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type', 'created_at', 'updated_at', 'project']
        read_only_fields = ['created_at']
