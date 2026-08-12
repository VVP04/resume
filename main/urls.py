from django.urls import path

from .views import (
    AboutView,
    ContactView,
    HomeView,
    PortfolioDetailView,
    PortfolioListView,
    ResumeView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('about/', AboutView.as_view(), name='about'),

    path('resume/', ResumeView.as_view(), name='resume'),

    path(
        'portfolio/',
        PortfolioListView.as_view(),
        name='portfolio_list',
    ),

    path(
        'portfolio/<slug:slug>/',
        PortfolioDetailView.as_view(),
        name='portfolio_detail',
    ),

    path('contacts/', ContactView.as_view(), name='contacts'),
]