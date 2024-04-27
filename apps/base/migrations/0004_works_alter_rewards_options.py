# Generated by Django 5.0.4 on 2024-04-27 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rewards_delete_slide_settings_facebook_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название тайтла')),
                ('image_of_college', models.ImageField(upload_to='job_image/', verbose_name='Фото колледжа')),
                ('publication', models.DateField(verbose_name='Дата публикации')),
                ('description_of_college', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': '3)Прошлое место работы',
                'verbose_name_plural': '3)Прошлые места работы',
            },
        ),
        migrations.AlterModelOptions(
            name='rewards',
            options={'verbose_name': '2)Прогресс', 'verbose_name_plural': '2)Прогрессы'},
        ),
    ]
