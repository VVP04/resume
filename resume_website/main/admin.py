from django.contrib import admin

from .models import Education, Project, Skill

admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Education)