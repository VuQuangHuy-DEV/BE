# Generated by Django 4.2.3 on 2024-05-21 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rental', '0012_alter_baitimviec_ly_do'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baitimviec',
            name='ly_do',
            field=models.CharField(default='', max_length=150, null=True),
        ),
    ]
