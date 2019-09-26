from django.db import models

# Create your models here.


class Task(models.Model):
    STATUSES = (
        ('to-do', 'To Do'),
        ('in_progress', 'In Progress'),
        ('blocked', 'Blocked'),
        ('peer_review', 'Peer Review'),
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
    partner = models.CharField(max_length=200)  # should be foreignKey to partner db
    # partner = models.ForeignKey(Partner, blank=True, null=True, on_delete=models.PROTECT)
    description = models.TextField("description", max_length=2000, null=True, blank=True)
    resolution = models.TextField("resolution", max_length=2000, null=True, blank=True)
    deadline = models.DateField("deadline", null=True, blank=True)
    user = models.ForeignKey('auth.User', related_name='tasks_assigned', verbose_name='assigned to',
                             on_delete=models.SET_NULL, null=True, blank=True),
    state = models.CharField("state", max_length=20, choices=STATUSES, default='to-do'),
    priority = models.CharField("priority", max_length=20, choices=PRIORITIES, default='10_normal'),
    created_by = models.ForeignKey('auth.User', related_name='users_created', verbose_name='created by',
                                   on_delete=models.SET_NULL, null=True),
    created_at = models.DateTimeField("created at", auto_now_add=True, editable=True, blank=True),
    last_modified = models.DateTimeField("last modified", auto_now=True, editable=True, blank=True),

    def __str__(self):
        return "[%s] %s" % (self.number, self.title)

    @property
    def number(self):
        return "{:08d}".format(self.pk)

    # def save(self, *args, **kwargs):
    #     task_created = self.pk is None
    #     super().save(*args, **kwargs)
    #     if task_created:
    #         self.send_new_task_email()

    # def send_new_task_email(self):
    #     """
    #     Override with a custom email
    #     """
    #     emails_to = []
    #     if settings.TASKS_SEND_EMAILS_TO_PARTNERS and getattr(self, "partner", None) and self.partner.email:
    #         emails_to.append(self.partner.email)
    #     if settings.TASKS_SEND_EMAILS_TO_ASSIGNED and getattr(self, "user", None) and self.user.email:
    #         emails_to.append(self.user.email)
    #     if len(emails_to):
    #         logger.info("[Task #%s] Sending task creation email to: %s", self.number, emails_to)
    #         vals = {
    #             "id": self.number,
    #             "user": str(self.user) if getattr(self, "user", None) else '(Not assigned yet)',
    #             "title": self.title,
    #             "description": self.description or '-',
    #             "sign": settings.SITE_HEADER,
    #         }
    #         if settings.TASKS_VIEWER_ENABLED:
    #             email_template = settings.MTASKS_EMAIL_WITH_URL
    #             vals["url"] = self.get_tasks_viewer_url()
    #         else:
    #             email_template = settings.MTASKS_EMAIL_WITHOUT_URL
    #         try:
    #             send_mail(
    #                 '[{app}] [#{id}] New Task Created'.format(app=settings.APP_NAME, id=self.number),
    #                 email_template.format(**vals),
    #                 settings.APP_EMAIL,
    #                 emails_to,
    #             )
    #         except Exception as e:
    #             logger.warning("[Task #%s] Error trying to send the task creation email - %s: %s",
    #                            self.number, e.__class__.__name__, str(e))


class Item(models.Model):
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Check List"

    task = models.ForeignKey('taskapp.Task', on_delete=models.CASCADE)
    item_description = models.CharField("description", max_length=200)
    is_done = models.BooleanField("done?", default=False)

    def __str__(self):
        return self.item_description
# notes
# author=models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
# post=models.ForeignKey('blog.post', related_name='comments', on_delete=models.DO_NOTHING)
