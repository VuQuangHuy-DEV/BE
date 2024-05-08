# Generated by Django 4.2.3 on 2024-03-01 13:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0007_khachhang_idkh_nhanvien_idnv_and_more'),
        ('Booking', '0003_rename_bookingpost_baithue'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baithue',
            name='user',
        ),
        migrations.AddField(
            model_name='baithue',
            name='khach_hang',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='Authentication.khachhang'),
        ),
    ]
