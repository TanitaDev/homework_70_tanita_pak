from django.contrib import admin
from webapp.models import *


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'status', 'type', 'created_at', 'updated_at']


class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']


class TypeAdmin(admin.ModelAdmin):
    list_display = ['name']


class TypeProject(admin.ModelAdmin):
    list_display = ['id', 'name', 'start_date', 'finish_date']


admin.site.register(Task, TaskAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Project, TypeProject)
