from django.views.generic import DetailView, ListView, TemplateView

from .models import Education, Project


class HomeView(TemplateView):
    """Home page."""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['education_list'] = Education.objects.all()
        return context


class AboutView(TemplateView):
    """About page."""

    template_name = 'main/about.html'


class ResumeView(TemplateView):
    """Resume page."""

    template_name = 'main/resume.html'


class PortfolioListView(ListView):
    """All projects and cases."""

    model = Project
    template_name = 'main/portfolio_list.html'
    context_object_name = 'projects'


class PortfolioDetailView(DetailView):
    """Individual project or case."""

    model = Project
    template_name = 'main/portfolio_detail.html'
    context_object_name = 'project'


class ContactView(TemplateView):
    """Contact page."""

    template_name = 'main/contacts.html'