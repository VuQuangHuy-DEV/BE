# Generated by Django 4.2.3 on 2024-03-01 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rental', '0005_remove_baitimviec_model_remove_baitimviec_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Brand',
        ),
    ]