# Generated by Django 2.2 on 2019-04-23 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dersler', '0003_auto_20190423_0120'),
        ('ogrenci', '0003_auto_20190423_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='ogrenci_dersleri',
            fields=[
                ('Id_dersogrenci', models.AutoField(primary_key=True, serialize=False, verbose_name='Id')),
                ('ders', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dersogrenci', to='dersler.Dersler', verbose_name='Ders')),
                ('ogrenci', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ogrencis', to='ogrenci.Ogrenci', verbose_name='Öğrenci')),
            ],
        ),
    ]