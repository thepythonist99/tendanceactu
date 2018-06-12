import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from tendance_actu.settings import NUMBER_OF_STARS

# Create your models here.


class Category(models.Model):
    name = models.CharField(_('Music category name'), max_length=60, unique=True, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return "%s" % self.name

    @classmethod
    def get_categories(cls):
        categories = Category.objects.all()
        return categories


class Artist(models.Model):
    name = models.CharField(_('Artist name'), max_length=60, blank=False, null=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return "%s" % self.name

    @classmethod
    def get_artists(cls):
        artists = Artist.objects.all()
        return artists


class Music(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Music category'))
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name=_('Song artist'))
    title = models.CharField(_('Music title'), max_length=60)
    song = models.FileField(_('MP3 audio sound'), upload_to='songs/', blank=True, null=False)
    video = models.FileField(_('MP4 video song'), upload_to='videos/', blank=True, null=False, default='')
    release_date = models.DateField(_('Release date'))
    num_stars = models.IntegerField(_('Number of stars'), default=1, choices=NUMBER_OF_STARS)

    class Meta:
        ordering = ['artist', 'title', 'song', 'release_date']

    def __str__(self):
        return "%s: %s" % (self.artist, self.song)

    @classmethod
    def get_musics(cls):
        musics = Music.objects.all()[:10]
        return musics

    def get_release_date(self):

        return Music.release_date

    def calculate_music_age(self):
        release_date = Music.release_date
        age = datetime.date.today() - self.get_release_date()
        print(release_date)

        return age
