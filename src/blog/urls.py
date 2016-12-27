from django.conf.urls import url
from .views import (post_list, view_category, view_post, view_author)

urlpatterns = [
    url(r'^$', post_list, name="list"),
    url(r'^view/(?P<slug>[^\.]+).html', view_post, name='detail'),
    url(r'^category/(?P<slug>[^\.]+).html', view_category, name="category"),
    url(r'^author/(?P<slug>[^\.]+).html', view_author, name="author"),

]

