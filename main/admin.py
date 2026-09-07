from django.contrib import admin

from .models import Skill, SkillCategory, Education, Experience


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = (
        "specialty",
        "degree",
        "education_type",
        "institution",
        "start_year",
        "end_year",
        "description",
        "document_url",
    )
    list_filter = ("education_type",)
    search_fields = (
        "specialty",
        "degree",
        "institution",
    )
    ordering = ("start_year",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display=(
        "position",
        "company",
        "start_year",
        "end_year",
        "description",
    )
    search_fields=(
        'position',
        'company',
    )
    ordering = ("start_year",)