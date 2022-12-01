from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField('auth.User', null=True, blank=True)


class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255, null=False)
    publication_date = models.DateTimeField(auto_now_add=True, null=False)
    short_text = models.CharField(max_length=255, null=False)
    text = models.TextField(null=False)

    topic = models.ForeignKey(Topic, null=True, blank=True, on_delete=models.SET_NULL)
