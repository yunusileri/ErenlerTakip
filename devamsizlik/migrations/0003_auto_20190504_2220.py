# Generated by Django 2.2 on 2019-05-04 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devamsizlik', '0002_auto_20190504_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devamsizlik',
            name='devamsizlik_tarihi',
            field=models.CharField(default='2019-05-04', max_length=10, verbose_name='Tarih'),
        ),
    ]
