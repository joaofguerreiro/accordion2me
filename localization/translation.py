# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from modeltranslation.translator import register, TranslationOptions
from localization.models import Country, Language, District, County


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Language)
class LanguageTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(District)
class DistrictTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(County)
class CountyTranslationOptions(TranslationOptions):
    fields = ('name',)
