# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Country(models.Model):
    alpha2 = models.CharField(_('ISO alpha-2'), max_length=2, primary_key=True)
    name = models.CharField(_('name'), max_length=128)
    num_code = models.PositiveSmallIntegerField(_('ISO numeric'), null=True)
    alpha3 = models.CharField(max_length=3, unique=True, help_text="ISO 3166-1 Alpha-3 Code")
    phone = models.CharField(max_length=3, help_text=_("Phone Indicative"))

    class Meta:
        ordering = ('name',)
        db_table = "localization_country"
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    class Menu:
        icon = "fa fa-flag"

    def __str__(self):
        return u"%s" % self.name


@python_2_unicode_compatible
class District(models.Model):
    name = models.CharField(_("Name"), max_length=250)

    class Meta:
        db_table = "localization_district"
        verbose_name = _("District")
        verbose_name_plural = _("Districts")
        ordering = ('name',)

    def __str__(self):
        return "%s" % self.name


@python_2_unicode_compatible
class County(models.Model):
    name = models.CharField(_("Name"), max_length=250)
    district = models.ForeignKey(District, verbose_name=_("District"))

    class Meta:
        db_table = "localization_county"
        verbose_name = _("County")
        verbose_name_plural = _("Counties")
        ordering = ('name',)

    def __str__(self):
        return "%s" % self.name


@python_2_unicode_compatible
class Language(models.Model):
    code = models.CharField(_("Abbreviation"), max_length=10, primary_key=True)
    name = models.CharField(_("Name"), max_length=250)

    class Meta:
        db_table = "localization_language"
        verbose_name = _("Language")
        verbose_name_plural = _("Languages")
        ordering = ('name',)

    def __str__(self):
        return "%s" % self.name
