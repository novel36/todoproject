# Generated by Django 2.2.20 on 2022-04-04 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20220404_0507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='todo_date',
        ),
    ]
