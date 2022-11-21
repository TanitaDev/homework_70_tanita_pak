from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializer import TaskSerializer
from webapp.models import Task


class TaskView(APIView):
    def get(self, request, *args, **kwargs):
        objects = Task.objects.all()
        serializer = TaskSerializer(objects, many=True)
        return Response(serializer.data)


class TaskDetailView(APIView):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)


class TaskUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        task = Task.objects.get(pk=pk)

        serializer = TaskSerializer(data=request.data, instance=task)
        if serializer.is_valid():
            task = serializer.save()
            return Response(serializer.data)


class TaskDeleteView(APIView):
    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(data=request.data)
        task.delete()
        if serializer.is_valid():
            task = serializer.save()
            return Response(serializer.data['pk'])
