from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length =255,
        verbose_name ='Название сайта'
    )
    logo = models.ImageField(
        upload_to='settings_image/',
        verbose_name='Логотип'
    )
    discrition = models.TextField(
        verbose_name='Описание сайта'
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='Номер телефона'
    )
    locate = models.CharField(
        max_length=255,
        verbose_name='Адрес'
    )
    email = models.EmailField(
        verbose_name='Почта'
    )
    instagram = models.URLField(
        verbose_name='Ссылка на инстаграм',
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "1) Основная настройка"
        verbose_name_plural = "1) Основные параметры"


class Slide(models.Model):
    image = models.ImageField(
        upload_to= 'PHOTO/',
        verbose_name= ' photo'
    )