# Generated by Django 2.2.20 on 2022-04-03 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20220403_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='todo_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
