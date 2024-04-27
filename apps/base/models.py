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
    facebook = models.URLField(
        verbose_name='Ссылка на на фейсбок',
    )
    whatsapp = models.URLField(
        verbose_name='Ссылка на ватсап',
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "1) Основная настройка"
        verbose_name_plural = "1) Основные параметры"

class Rewards(models.Model):
    title = models.CharField(
        max_length=500,
        verbose_name='Прогресс'
    )
    subtitle = models.TextField(
        verbose_name='Описание прогресса'
    )
    year = models.DateField(
        verbose_name='Дата'
    )
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = '2)Прогресс'
        verbose_name_plural = '2)Прогрессы'

class Works(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название тайтла'
    )
    image_of_college = models.ImageField(
        upload_to='job_image/',
        verbose_name = 'Фото колледжа'
    )
    publication = models.DateField(
        verbose_name='Дата публикации'
    )
    description_of_college = models.TextField(
        verbose_name='Описание'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '3)Прошлое место работы'
        verbose_name_plural = '3)Прошлые места работы'

class Experience(models.Model):
    description = models.TextField(
        verbose_name='Описание опыта работы'
    )

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name = '4)Опыт работы'
        verbose_name_plural = '4)Опыты работы'

class ExpModel(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='название'
    )
    desc = models.TextField(
        verbose_name='описание'
    )
    def __str__(self):
        return self.title

    class Meta:
        verbose_name='5)опыт'
        verbose_name_plural='5)опыт'

class Journal(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='название'
    )
    desc = models.TextField(
        verbose_name='описание'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='6)Журнал'
        verbose_name_plural='6)Журнал'

class Research(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='название'
    )
    desc = models.TextField(
        verbose_name='описание'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='7)Исследовать'
        verbose_name_plural='7)Исследовать'

class Latest(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='название'
    )
    image_of_college = models.ImageField(
        upload_to='job_image/',
        verbose_name = 'Фото '
    )
    desc = models.TextField(
        verbose_name='описание'
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name='8)Последние блоги'
        verbose_name_plural='8)Последние блоги'


 