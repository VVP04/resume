from django.db import models


class Project(models.Model):
    TYPE_CHOICES = [
        ('project', 'Проект'),
        ('case', 'Кейс'),
    ]
    title = models.CharField(max_length=200, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='URL-адрес')
    type = models.CharField(
        max_length=10, choices=TYPE_CHOICES, verbose_name='Тип'
    )
    short_description = models.CharField(
        max_length=300, verbose_name='Краткое описание'
    )
    description = models.TextField(verbose_name='Полное описание')
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True,
        verbose_name='Изображение',
    )
    link = models.URLField(blank=True, verbose_name='Ссылка на проект')
    github_link = models.URLField(
        blank=True, verbose_name='Ссылка на GitHub'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания'
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name


class Education(models.Model):
    institution = models.CharField(
        max_length=200, verbose_name='Учебное заведение'
    )
    degree = models.CharField(
        max_length=200, verbose_name='Степень / Специальность'
    )
    start_date = models.DateField(verbose_name='Начало')
    end_date = models.DateField(
        blank=True, null=True, verbose_name='Окончание'
    )
    description = models.TextField(blank=True, verbose_name='Описание')

    class Meta:
        ordering = ['-start_date']
        verbose_name = 'Образование'
        verbose_name_plural = 'Образование'

    def __str__(self):
        return f'{self.degree} — {self.institution}'