# Generated by Django 4.1.3 on 2022-11-20 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provinsi', models.CharField(max_length=120, null=True, verbose_name='Provinsi')),
                ('tarif_motor', models.CharField(blank=True, max_length=120, verbose_name='Tarif Motor')),
                ('tarif_mobil', models.CharField(blank=True, max_length=120, verbose_name='Tarif Mobil')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
