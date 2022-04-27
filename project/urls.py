from django.urls import path

from project import views
urlpatterns = [
    path('', views.DashboardView.as_view(), name='home'),
]
