# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class LocalizationConfig(AppConfig):
    name = 'localization'
    label = "localization"
    verbose_name = _("Localization")
