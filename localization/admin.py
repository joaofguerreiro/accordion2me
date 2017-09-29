# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from localization.models import Country, Language, District, County


class CountryAdmin(TranslationAdmin):
    pass


class LanguageAdmin(TranslationAdmin):
    pass


class CountyInlineAdmin(admin.TabularInline):
    model = County
    extra = 0
    min_num = 0


class DistrictAdmin(TranslationAdmin):
    inlines = (
        CountyInlineAdmin,
    )

class CountyAdmin(TranslationAdmin):
    pass


admin.site.register(Country, CountryAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(County, CountyAdmin)
