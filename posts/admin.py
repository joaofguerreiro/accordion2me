# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from posts.models import UserProfile, Category, Tag, Post, Comment


class UserProfileAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(TranslationAdmin):
    fields = ('name', 'short_description', 'is_active')
    list_display = ('name', 'short_description', 'is_active')
    list_filter = ('is_active', )
    search_fields = ('name', )


class TagAdmin(TranslationAdmin):
    fields = ('name', 'short_description', 'color', 'is_active')
    list_display = ('name', 'short_description', 'color', 'is_active')
    list_filter = ('is_active', )
    search_fields = ('name', 'color')


class CommentInlineAdmin(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    inlines = (CommentInlineAdmin,)
    fields = ('author', 'title', 'content', 'tags',)
    list_display = ('author', 'title',)
    list_search = ('author', 'title',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
