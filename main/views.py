from django.views.generic import DetailView, ListView, TemplateView

from .models import Education, Project, Skill


class HomeView(TemplateView):
    """Главная страница"""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['education_list'] = Education.objects.all()
        return context


class PortfolioListView(ListView):
    """Все проекты и кейсы"""
    model = Project
    template_name = 'main/portfolio_list.html'
    context_object_name = 'projects'


class PortfolioDetailView(DetailView):
    """Отдельный проект или кейс"""
    model = Project
    template_name = 'main/portfolio_detail.html'
    context_object_name = 'project'


class SkillsView(TemplateView):
    """Страница навыков"""
    template_name = 'main/skills.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['skills'] = Skill.objects.all()
        return context


class ContactView(TemplateView):
    """Контакты"""
    template_name = 'main/contacts.html'