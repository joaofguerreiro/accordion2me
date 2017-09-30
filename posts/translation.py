# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from modeltranslation.translator import register, TranslationOptions

from posts.models import Category, Tag


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description')


@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description')
