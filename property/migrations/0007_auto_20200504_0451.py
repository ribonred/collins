# Generated by Django 2.2.7 on 2020-05-04 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_auto_20191114_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prosesbangun',
            name='keterangan',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='uangmuka',
            name='keterangan',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
