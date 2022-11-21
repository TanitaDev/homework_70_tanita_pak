from django.urls import path

from api.views import TaskView, TaskCreateView, TaskDetailView

urlpatterns = [
    path('tasks/', TaskView.as_view(), name='tasks'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='create'),
]
