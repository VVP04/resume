from django.views.generic import TemplateView

from .models import SkillCategory, Education, Experience


class HomeView(TemplateView):

    template_name = 'home.html'


class AboutView(TemplateView):

    template_name = 'about.html'


class ResumeView(TemplateView):

    template_name = 'resume.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["skill_categories"] = SkillCategory.objects.prefetch_related(
            "skills"
        )

        context["educations"] = Education.objects.all()

        context["experiences"] = Experience.objects.all()

        return context