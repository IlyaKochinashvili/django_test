from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from blog.views import BlogListView, user_page, PostsViewSet

router = routers.DefaultRouter()
router.register(r'personal_account', PostsViewSet)

urlpatterns = [
    path('', BlogListView.as_view(), name='blog'),
    path('user_page', user_page, name='user_page'),
    url(r'^', include(router.urls)),
]
