from django.db import models

# Create your models here.

class Task(models.Model):
	TASK_TYPE = ((1, 'Meeting'),
		        (2, 'Interview'),
		        (3, 'Other'))
	task_name = models.CharField(max_length=50)
	schedule_date = models.DateTimeField()
	description = models.CharField(max_length=200)
	task_type = models.IntegerField(choices=TASK_TYPE, default=3)
	email_id = models.CharField(max_length=300, blank=True, null=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return '%s' % self.task_name

	class Meta:
		default_permissions = ('add', 'change', 'delete', 'view')
		ordering = ('created_at',)
		db_table = 'task'
		app_label = 'todo'