# Generated by Django 2.2 on 2019-05-04 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dersler', '0003_auto_20190423_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dersler',
            name='ders_yili',
            field=models.CharField(max_length=4, null=True, verbose_name='Ders Yılı'),
        ),
    ]
