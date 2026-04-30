from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views
urlpatterns =[
    path("",views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.AllPostsView.as_view(), name="posts-page"),

    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-details-page"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)