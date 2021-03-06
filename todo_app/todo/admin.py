from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
	model = Task
	list_display = ['task_name', 'schedule_date', 'description']

admin.site.register(Task, TaskAdmin)
