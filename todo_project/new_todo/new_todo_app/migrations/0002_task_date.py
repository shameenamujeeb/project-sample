# Generated by Django 4.2.7 on 2023-12-01 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1990-12-22'),
            preserve_default=False,
        ),
    ]
