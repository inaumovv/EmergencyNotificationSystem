# Generated by Django 4.2.11 on 2024-06-20 13:46

import apps.contact_groups.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_groups', '0003_remove_contactgroup_user_contactgroup_object_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactgroup',
            old_name='name',
            new_name='group_name',
        ),
        migrations.RemoveField(
            model_name='contactgroup',
            name='object_name',
        ),
        migrations.AddField(
            model_name='contactgroup',
            name='file_id',
            field=models.CharField(default=apps.contact_groups.models.default_uid, unique=True, verbose_name='ID файла'),
        ),
        migrations.AddField(
            model_name='contactgroup',
            name='filename',
            field=models.CharField(default='default', max_length=122, verbose_name='Имя объекта'),
        ),
    ]
