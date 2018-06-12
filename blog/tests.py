import datetime

from django.test import TestCase

from .models import Entry

# Create your tests here.


class EntryModelTests(TestCase):

    def test_was_released_recently_with_future_entry(self):
        """
        was_released_recently returns False for entries whose
        release_date is in the future
        :return: False
        """
        date = datetime.date.today() + datetime.timedelta(days=30)
        future_entry = Entry(release_date=date)

        self.assertIs(future_entry.was_released_recently(), False)

    def test_was_released_recently_with_old_entry(self):
        """
        was_released_recently returns False for entries whose
        release_date is older than one day
        :return: False
        """
        date = datetime.date.today() - datetime.timedelta(days=1, seconds=1)
        old_entry = Entry(release_date=date)

        self.assertIs(old_entry.was_released_recently(), False)

    def test_was_released_recently_with_recent_question(self):
        """
        was_released_recently returns True for entries whose
        release_date is younger than one day
        :return: True
        """
        date = datetime.date.today() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_entry = Entry(release_date=date)

        self.assertIs(recent_entry.was_released_recently(), True)
