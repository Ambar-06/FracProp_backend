from django.urls import path

from . import views

urlpatterns = [
    path("", views.PropertyView.as_view(), name="property"),
    path("approval-requests/", views.ApprovalRequestView.as_view(), name="approval_request"),
    path("approval-requests/<str:request_id>/", views.SingleApprovalRequestView.as_view()),
    path("<str:property_id>/", views.SinglePropertyView.as_view()),
    path(
        "<str:property_id>/invest/",
        views.SinglePropertyView.as_view(),
    ),
]
