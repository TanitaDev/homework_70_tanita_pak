from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializer import TaskSerializer
from webapp.models import Task


class TaskDetailView(APIView):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)


class TaskUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        object = get_object_or_404(Task, pk=kwargs.get('pk'))

        serializer = TaskSerializer(object, data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class TaskDeleteView(APIView):
    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(data=request.data)
        task.delete()
        if serializer.is_valid():
            task = serializer.save()
            return Response(data={"id": task.id})
        else:
            return Response(serializer.errors, status=404)
