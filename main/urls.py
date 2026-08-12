from django.urls import path

from .views import (
    ContactView,
    HomeView,
    PortfolioDetailView,
    PortfolioListView,
    SkillsView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('portfolio/', PortfolioListView.as_view(), name='portfolio_list'),
    path(
        'portfolio/<slug:slug>/',
        PortfolioDetailView.as_view(),
        name='portfolio_detail',
    ),
    path('skills/', SkillsView.as_view(), name='skills'),
    path('contacts/', ContactView.as_view(), name='contacts'),
]