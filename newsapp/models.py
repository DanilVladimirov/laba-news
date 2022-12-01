from django.db import models


class News(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255, null=False)
    publication_date = models.DateTimeField(auto_now_add=True, null=False)
    short_text = models.CharField(max_length=255, null=False)
    text = models.TextField(null=False)
