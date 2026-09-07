from django.db import models


class SkillCategory(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название",
    )

    class Meta:
        verbose_name = "Категория навыков"
        verbose_name_plural = "Категории навыков"

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название",
    )

    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
        related_name="skills",
        verbose_name="Категория",
    )

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.name


class Education(models.Model):
    class EducationType(models.TextChoices):
        HIGHER = "higher", "Высшее образование"
        ADDITIONAL = "additional", "Дополнительное образование"

    education_type = models.CharField(
        "Тип образования",
        max_length=20,
        choices=EducationType.choices,
    )
    specialty = models.CharField(
        "Специальность",
        max_length=255,
    )
    degree = models.CharField(
        "Степень",
        max_length=100,
    )
    start_year = models.PositiveIntegerField(
        "Год начала",
    )
    end_year = models.PositiveIntegerField(
        "Год окончания",
    )
    institution = models.CharField(
        "Учебное заведение",
        max_length=255,
    )
    description = models.TextField(
        "Описание",
        blank=True,
    )
    document_url = models.URLField(
        "Ссылка на документ",
        blank=True,
    )

    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Образование"
        ordering = ["start_year"]

    def __str__(self):
        return f"{self.specialty} — {self.degree}"


class Experience(models.Model):
    position = models.CharField(
        "Должность",
        max_length=255,
    )
    company = models.CharField(
        "Компания",
        max_length=255,
    )
    start_year = models.PositiveIntegerField(
        "Год начала",
    )
    end_year = models.PositiveIntegerField(
        "Год окончания",
    )
    description = models.TextField(
        "Описание",
        blank=True,
    )

    class Meta:
        verbose_name = "Опыт"
        verbose_name_plural = "Опыт"
        ordering = ["start_year"]

    def __str__(self):
        return f"{self.position}"
    
    @property
    def description_list(self):
        if not self.description:
            return []
        
        return [
            item.strip() 
            for item in self.description.split('.') 
            if item.strip()
        ]