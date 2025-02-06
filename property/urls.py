from django.urls import path

from . import views

urlpatterns = [
    path("", views.PropertyView.as_view(), name="property"),
    path("<str:property_id>", views.SinglePropertyView.as_view()),
    path(
        "<str:property_id>/invest/",
        views.SinglePropertyView.as_view(),
    ),
]
