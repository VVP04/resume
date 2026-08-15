from django.views.generic import DetailView, ListView, TemplateView

from .models import Project


class HomeView(TemplateView):

    template_name = 'home.html'


class AboutView(TemplateView):

    template_name = 'about.html'


class ResumeView(TemplateView):

    template_name = 'resume.html'


class PortfolioListView(ListView):

    model = Project
    template_name = 'portfolio_list.html'
    context_object_name = 'projects'


class PortfolioDetailView(DetailView):

    model = Project
    template_name = 'portfolio_detail.html'
    context_object_name = 'project'


class ContactView(TemplateView):

    template_name = 'contacts.html'