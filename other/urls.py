from django.urls import path

from . import views

urlpatterns = [
    path("blogs/", views.BlogView.as_view(), name="blogs"),
    path("blogs/<str:blog_id>", views.SingleBlogView.as_view(), name="single-blog"),
]