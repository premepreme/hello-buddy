# Generated by Django 4.1.3 on 2022-11-29 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Hello_Buddy", "0003_alter_event_name_alter_event_place"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="name",
            field=models.CharField(max_length=30, verbose_name="Name"),
        ),
    ]
