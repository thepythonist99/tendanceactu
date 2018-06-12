from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from blog.models import Person, Entry, Category

# Register your models here.


class PersonInline(admin.TabularInline):
    model = Person
    extra = 1


class CategoryInline(admin.TabularInline):
    model = Category
    extra = 1


class EntryAdmin(admin.ModelAdmin):
    list_filter = (_('published'), _('title'))
    list_display = ('title', 'release_date', 'category', 'was_released_recently')
    fieldsets = [
        (_('Entry base information'), {'fields': ['title', 'slug', 'brief_content', 'content']}),
        (_('Release date information'), {'fields': ['release_date']}),
        (_('Release information'), {'fields': ['published']}),
        (_('Entry Tags'), {'fields': ['tags']}),
    ]
    # inlines = [PersonInline, CategoryInline]


class PersonAdmin(admin.ModelAdmin):
    list_filter = (_('user_name'), _('last_name'))
    list_display = ('user_name', 'first_name', 'last_name')


class CategoryAdmin(admin.ModelAdmin):
    list_filter = (_('name'), _('date_created'))
    list_display = ('name', 'date_created')


admin.site.register(Person, PersonAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)
