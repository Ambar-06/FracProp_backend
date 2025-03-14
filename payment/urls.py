from django.urls import path

from . import views

urlpatterns = [
    path("transactions", views.TransactionViews.as_view(), name="transactions"),
]