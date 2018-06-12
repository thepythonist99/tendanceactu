from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from download.models import Category, Artist, Music

# Register your models here.


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


class ArtistInline(admin.TabularInline):
    model = Artist
    extra = 1


class MusicAdmin(admin.ModelAdmin):
    fieldsets = [
        (_('Music category'), {'fields': ['category']}),
        (_('Artist name'), {'fields': ['artist']}),
        (_('Music title'), {'fields': ['title']}),
        (_('Release date information'), {'fields': ['release_date']}),
        (_('MP3 sound'), {'fields': ['song']}),
        (_('MP4 song'), {'fields': ['video']}),
        (_('Number of stars'), {'fields': ['num_stars']}),
    ]
    # inlines = [CategoryInline, ArtistInline]
    list_display = ('title', 'release_date')


class ArtistAdmin(admin.ModelAdmin):
    fieldsets = [
        (_('Artist name'), {'fields': ['name']}),
    ]


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (_('Category name'), {'fields': ['name']}),
    ]


admin.site.register(Music, MusicAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Artist, ArtistAdmin)
