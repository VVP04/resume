from django.urls import path

from .views import (
    AboutView,
    HomeView,
    ResumeView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('about/', AboutView.as_view(), name='about'),

    path('resume/', ResumeView.as_view(), name='resume'),
]