# Generated by Django 3.2.9 on 2021-12-11 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20211211_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='blog_image',
            field=models.ImageField(default='', upload_to='{% static "images/posts" %}'),
        ),
    ]