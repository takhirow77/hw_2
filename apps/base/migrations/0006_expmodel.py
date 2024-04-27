# Generated by Django 5.0.4 on 2024-04-27 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('desc', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'опыт',
                'verbose_name_plural': 'опыт',
            },
        ),
    ]
