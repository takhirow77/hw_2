# Generated by Django 5.0.4 on 2024-04-27 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_works_alter_rewards_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание опыта работы')),
            ],
            options={
                'verbose_name': '4)Опыт работы',
                'verbose_name_plural': '4)Опыты работы',
            },
        ),
    ]
