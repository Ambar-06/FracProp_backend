from . import views
from django.urls import path


urlpatterns = [
    path("property", views.PropertyView.as_view(), name="property"),
    path("property/<str:property_id>", views.SinglePropertyView.as_view()),
    path(
        "property/<str:property_id>/invest",
        views.SinglePropertyView.as_view({"post": "invest"}),
    ),
]
