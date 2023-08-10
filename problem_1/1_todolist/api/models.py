from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=80)
    date_created = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_created']
        db_table = 'task'
    
    def __str__(self):
        return self.title