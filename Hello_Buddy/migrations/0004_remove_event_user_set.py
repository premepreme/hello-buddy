# Generated by Django 4.1.1 on 2022-10-21 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Hello_Buddy", "0003_manytomany"),
    ]

    operations = [
        migrations.RemoveField(model_name="event", name="user_set",),
    ]
