# Generated by Django 4.1.3 on 2022-12-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('short_text', models.CharField(max_length=255)),
                ('text', models.TextField()),
            ],
        ),
    ]
