# Generated by Django 4.2.3 on 2024-04-24 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rental', '0009_rename_khach_hang_baitimviec_khach_hang_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baitimviec',
            name='image_desc1',
        ),
    ]
