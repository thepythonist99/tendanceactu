import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Event(models.Model):
    title = models.CharField(_('Event title'), max_length=60)
    slug = models.SlugField(_('Event slug'), max_length=60, unique=True)
    content = models.TextField(_('Event content'))
    date = models.DateField(_('Event date'))
    published = models.BooleanField(_('Publish event ?'))

    class Meta:
        ordering = ['title']

    def __str__(self):
        return "%s->%s" % (self.title, self.date)

    @classmethod
    def get_events(cls):
        events = Event.objects.filter(published=True)
        return events

    def was_published(self):
        if Event.published:
            return True
    was_published.admin_order_field = 'date'
    was_published.boolean = True
    was_published.short_description = 'Published ?'
