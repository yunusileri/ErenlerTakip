# Generated by Django 2.2 on 2019-04-22 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogrenci', '0002_auto_20190422_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ogrenci',
            name='aol_no',
            field=models.CharField(default=1, max_length=10, verbose_name='AOL Num'),
            preserve_default=False,
        ),
    ]