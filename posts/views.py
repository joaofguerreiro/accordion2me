# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView, DetailView, CreateView

from posts.forms import PostCreateForm
from posts.models import Post


class PostIndexView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'posts/index_view.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail_view.html'


class PostCreateView(CreateView):
    template_name = 'posts/create.html'
    model = Post
    form_class = PostCreateForm

    def get_form_kwargs(self):
        kwargs = super(PostCreateView, self).get_form_kwargs()
        kwargs['initial'].update({
            'author': self.request.user
        })
        return kwargs
