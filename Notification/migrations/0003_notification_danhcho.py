# Generated by Django 4.2.3 on 2024-04-10 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notification', '0002_rename_is_read_notification_da_doc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='danhcho',
            field=models.TextField(default='personal', max_length=10),
        ),
    ]
