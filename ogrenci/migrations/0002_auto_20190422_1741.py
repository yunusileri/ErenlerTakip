# Generated by Django 2.2 on 2019-04-22 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ogrenci', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ogrenci',
            old_name='adSoyad',
            new_name='ad_soyad',
        ),
        migrations.RenameField(
            model_name='ogrenci',
            old_name='aolNo',
            new_name='aol_no',
        ),
    ]
