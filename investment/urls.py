from django.urls import path

from . import views

urlpatterns = [
    path("", views.InvestmentView.as_view(), name="investments"),
]

