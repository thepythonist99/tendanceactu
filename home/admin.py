from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from home.models import Event

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_filter = (_('title'), _('published'))
    list_display = ('title', 'date', 'was_published')


admin.site.register(Event, EventAdmin)
