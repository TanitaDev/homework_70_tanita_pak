from django.urls import path

from api.views import *

urlpatterns = [
    path('tasks/', TaskView.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetailView.as_view(), name='task'),
    path('update/<int:pk>', TaskUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='delete')
]
