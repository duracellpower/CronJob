from django.db import models


class CronJob(models.Model):
    # title, address
    title = models.TextField(max_length=30)
    url = models.TextField(max_length=256)

    # login
    userName = models.TextField(max_length=30, null=False, default='')
    password = models.CharField(max_length=50, null=False, default='')

    # set time and date
    schedule = models.CharField(max_length= 50)

    # messages
    messageFail = models.BooleanField(default=False)
    messageSuccess = models.BooleanField(default=False)
    messageTooMuchFailures = models.BooleanField(default=False)

    # save
    saveAnswer = models.BooleanField(default=False)


