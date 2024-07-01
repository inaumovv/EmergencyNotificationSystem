# Generated by Django 4.2.11 on 2024-06-17 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_groups', '0002_alter_contactgroup_options_remove_contactgroup_url_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactgroup',
            name='user',
        ),
        migrations.AddField(
            model_name='contactgroup',
            name='object_name',
            field=models.CharField(blank=True, max_length=122, null=True, unique=True, verbose_name='Имя объекта'),
        ),
    ]
