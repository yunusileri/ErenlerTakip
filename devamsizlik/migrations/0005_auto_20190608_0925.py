# Generated by Django 2.2 on 2019-06-08 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devamsizlik', '0004_devamsizlik_saat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devamsizlik',
            name='devamsizlik_tarihi',
            field=models.CharField(default='2019-06-08', max_length=10, verbose_name='Tarih'),
        ),
        migrations.AlterField(
            model_name='devamsizlik',
            name='saat',
            field=models.CharField(default='09:00', max_length=5, verbose_name='Saat'),
        ),
    ]