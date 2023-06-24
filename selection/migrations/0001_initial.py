# Generated by Django 4.1.5 on 2023-02-24 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('items', models.ManyToManyField(to='ads.ad')),
            ],
            options={
                'verbose_name': 'Подборка объявлений',
                'verbose_name_plural': 'Подборки объявлений',
            },
        ),
    ]
