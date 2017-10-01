# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from posts.models import Post


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'tags', 'title', 'content')
        widgets = {
            'author': forms.HiddenInput,
        }

    def __init__(self, *args, **kwargs):
        super(PostCreateForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(PostCreateForm, self).clean()
        return cleaned_data
