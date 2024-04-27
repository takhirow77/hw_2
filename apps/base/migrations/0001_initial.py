# Generated by Django 5.0.4 on 2024-04-25 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название сайта')),
                ('logo', models.ImageField(upload_to='settings_image/', verbose_name='Логотип')),
                ('discrition', models.TextField(verbose_name='Описание сайта')),
                ('phone', models.CharField(max_length=255, verbose_name='Номер телефона')),
                ('locate', models.CharField(max_length=255, verbose_name='Адрес')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('instagram', models.URLField(verbose_name='Ссылка на инстаграм')),
            ],
            options={
                'verbose_name': '1) Основная настройка',
                'verbose_name_plural': '1) Основные параметры',
            },
        ),
    ]