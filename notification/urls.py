from django.urls import path

from . import views

urlpatterns = [
    path("templates", views.TemplateView.as_view(), name="templates"),
]