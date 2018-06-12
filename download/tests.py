import datetime

from django.test import TestCase

from download.models import Music

# Create your tests here.


class MusicModelTest(TestCase):

    def test_calculate_music_age(self):
        """
        Returns the number of days of a given music
        after released date.
        :return: days
        """
        self.days = datetime.date.today() - Music.release_date

        return self.days
