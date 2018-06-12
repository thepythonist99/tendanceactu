import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Person(models.Model):
    user_name = models.CharField(_("person's'username'"), max_length=50, unique=True)
    first_name = models.CharField(_("person's 'first name'"), max_length=50)
    last_name = models.CharField(_("person's 'last name'"), max_length=50)

    class Meta:
        ordering = ['last_name']
        app_label = 'blog'

    def __str__(self):
        return "%s" % self.user_name


class Category(models.Model):
    name = models.CharField(_("Category's name"), max_length=60, unique=True)
    date_created = models.DateField(_('Date created'), default=datetime.date.today())

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return "%s" % self.name


class Entry(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name=_("person publishing"))
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name=_("article Category"),
                                 default='')
    title = models.CharField(_('title of entry'), max_length=60, unique=True)
    slug = models.SlugField(_("url's slug"), max_length=60, unique=True)
    brief_content = models.TextField(_('brief description of content'), default='')
    content = models.TextField(_('entry content'))
    release_date = models.DateField(default=datetime.date.today())
    published = models.BooleanField(default=True)
    image = models.ImageField(_("entry's image"), upload_to='images/')
    tags = models.CharField(max_length=50, default='Article')

    class Meta:
        app_label = 'blog'
        ordering = ['release_date']

    def __str__(self):
        return "%s" % self.title

    @classmethod
    def get_entries(cls):
        entries = Entry.objects.all()
        return entries

    @classmethod
    def get_top_entries(cls):
        top_entries = Entry.objects.order_by('release_date').filter(published=True)[:10]
        return top_entries

    @classmethod
    def get_published_entries(cls):
        published_entries = Entry.objects.filter(published=True)[:10]
        return published_entries

    @classmethod
    def get_top_three_entries(cls):
        top_three_entries = Entry.objects.filter(published=True)[:3]
        return top_three_entries

    def was_released_recently(self):
        now = datetime.date.today()
        return now - datetime.timedelta(days=1) < self.release_date <= now
    was_released_recently.admin_order_field = 'release_date'
    was_released_recently.boolean = True
    was_released_recently.short_description = 'Released recently ?'
