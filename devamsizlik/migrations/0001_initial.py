# Generated by Django 2.2 on 2019-04-25 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ogrenci_dersleri', '0002_auto_20190425_1308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devamsizlik',
            fields=[
                ('Id_devamsizlik', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('devamsizlik_tarihi', models.DateTimeField(auto_now_add=True, verbose_name='Tarih')),
                ('ogrenci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Öğrenci', to='ogrenci_dersleri.ogrenci_dersleri', verbose_name='Öğrenci')),
            ],
        ),
    ]
