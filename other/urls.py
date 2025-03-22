from django.urls import path

from . import views

urlpatterns = [
    path("blogs/", views.BlogView.as_view(), name="blogs"),
    path("blogs/<str:blog_id>", views.SingleBlogView.as_view(), name="single-blog"),
    path("public/blogs/", views.OpenBlogView.as_view(), name="open-blogs"),
    path("public/blogs/<str:blog_id>", views.SingleOpenBlogView.as_view(), name="single-open-blog"),
    path("jobs/", views.JobView.as_view(), name="jobs"),
]