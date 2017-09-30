# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from localization.models import Country, Language, County


@python_2_unicode_compatible
class UserProfile(models.Model):
    user = models.ForeignKey(verbose_name=_('User'), to=User)
    picture = models.ImageField(verbose_name=_('Profile Picture'), upload_to='profile_pictures',
                                default='profile_pictures/default.jpg', null=True, blank=True)
    country = models.ForeignKey(verbose_name=_('Country'), to=Country, blank=True, null=True)
    language = models.ForeignKey(verbose_name=_('Language'), to=Language)
    county = models.ForeignKey(verbose_name=_('County'), to=County, blank=True, null=True)
    is_active = models.BooleanField(_('Active'), default=True, help_text=_(
        "Designates whether this category should be treated as active. Deselect this instead of deleting categories."))

    class Meta:
        db_table = 'posts_user_profile'
        verbose_name = _('User Profile')
        verbose_name_plural = _('User Profiles')

    def __str__(self):
        return "{}".format(self.user)


@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    short_description = models.CharField(verbose_name=_('Short Description'), max_length=200)
    is_active = models.BooleanField(_('Active'), default=True, help_text=_(
        "Designates whether this category should be treated as active. Deselect this instead of deleting categories."))

    class Meta:
        db_table = 'posts_category'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return "{}".format(self.name)


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    short_description = models.CharField(verbose_name=_('Short Description'), max_length=200)
    color = models.CharField(verbose_name=_('Color'), help_text="Only hex codes are allowed. Eg: #FFF", max_length=10)
    is_active = models.BooleanField(_('Active'), default=True, help_text=_(
        "Designates whether this category should be treated as active. Deselect this instead of deleting categories."))

    class Meta:
        db_table = 'posts_tag'
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')

    def __str__(self):
        return "{}".format(self.name)


@python_2_unicode_compatible
class Post(models.Model):
    author = models.ForeignKey(verbose_name=_('Author'), to=User)
    tags = models.ManyToManyField(verbose_name=_('Tags'), to=Tag)
    title = models.CharField(verbose_name=_('Name'), max_length=100)
    content = models.URLField(verbose_name=_('Content'), max_length=100)
    created_on = models.DateTimeField(verbose_name=_('Date Created'), auto_now_add=True)

    def __str__(self):
        return "{} by {}".format(self.title[:30], self.author)


@python_2_unicode_compatible
class Comment(models.Model):
    author = models.ForeignKey(verbose_name=_('Author'), to=User)
    post = models.ForeignKey(verbose_name=_('Post'), to=Post)
    content = models.URLField(verbose_name=_('Content'), max_length=100)
    created_on = models.DateTimeField(verbose_name=_('Date Created'), auto_now_add=True)
    votes = models.IntegerField(verbose_name=_('Votes'), default=0)

    class Meta:
        db_table = 'posts_comment'
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return "{} by {}".format(self.content[:30], self.author)


class Vote(models.Model):
    user = models.ForeignKey(verbose_name=_('Author'), to=User)
    comment = models.ForeignKey(verbose_name=_('Comment'), to=Comment)

    class Meta:
        db_table = 'posts_vote'
        verbose_name = _('Vote')
        verbose_name_plural = _('Votes')


class CommentVote(models.Model):
    user = models.ForeignKey(verbose_name=_('Author'), to=User)
    comment = models.ForeignKey(verbose_name=_('Comment'), to=Comment)

    class Meta:
        db_table = 'posts_comment_vote'
        verbose_name = _('Comment Vote')
        verbose_name_plural = _('Comment Votes')
