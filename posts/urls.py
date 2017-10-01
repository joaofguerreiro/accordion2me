# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from posts import views

urlpatterns = [
    url(r'^$', views.PostIndexView.as_view(), name='posts_index'),
    url(r'^post/create', views.PostCreateView.as_view(), name='post_create'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='post_detail'),

]
