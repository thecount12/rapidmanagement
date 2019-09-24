from django.db import models

# Create your models here.


class Task(models.Model):
    STATUSES = (
        ('to-do', 'To Do'),
        ('in_progress', 'In Progress'),
        ('blocked', 'Blocked'),
        ('done', 'Done'),
        ('dismissed', 'Dismissed')
    )

    PRIORITIES = (
        ('00_low', 'Low'),
        ('10_normal', 'Normal'),
        ('20_high', 'High'),
        ('30_critical', 'Critical'),
        ('40_blocker', 'Blocker')
    )

    title = models.CharField("title", max_length=200)
    partner = models.CharField()
    description = models.TextField("description", max_length=2000, null=True, blank=True)
    resolution = models.TextField("resolution", max_length=2000, null=True, blank=True)
    deadline = models.DateField("deadline", null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tasks_assigned', verbose_name='assigned to',
                             on_delete=models.SET_NULL, null=True, blank=True),
    state = models.CharField("state", max_length=20, choices=STATUSES, default='to-do'),
    priority = models.CharField("priority", max_length=20, choices=PRIORITIES, default='10_normal'),
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='users_created', verbose_name='created by',
                                   on_delete=models.SET_NULL, null=True),
    created_at = models.DateTimeField("created at", auto_now_add=True, editable=False),
    last_modified = models.DateTimeField("last modified", auto_now=True, editable=False),

    def __str__(self):
        return "[%s] %s" % (self.number, self.title)
