# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PostsConfig(AppConfig):
    name = 'posts'
    label = 'posts'
    verbose_name = _('Posts')
