# Generated by Django 3.2.5 on 2021-07-09 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
