from django.test import TestCase

from magazine.models import Magazine
from datetime import date

class MagazineTestCase(TestCase):
    def setUp(self):
        Magazine.objects.create()
        Magazine.objects.create()

    def test_first_publication_has_correct_issue_and_volume(self):
        """The first Magazine created is issue 1 of volume 1"""
        first_publication = Magazine.objects.get(pk=1)
        first_publication.publish()

        self.assertEqual(first_publication.volume, 1)
        self.assertEqual(first_publication.issue, 1)
    
    def test_publication_preserves_volume_and_increments_issue(self):
        """A Magazine published in the same year as another is the next issue of the same volume"""
        first_publication = Magazine.objects.get(pk=1)
        first_publication.publish()

        second_publication = Magazine.objects.get(pk=2)
        second_publication.publish()

        self.assertEqual(second_publication.volume, first_publication.volume)
        self.assertEqual(second_publication.issue, first_publication.volume + 1)

    def test_publication_increments_volume_and_resets_issue(self):
        """The first Magazine published in a given year is issue 1 of the next volume"""
        current_date = date.today()

        first_publication = Magazine.objects.get(pk=1)
        first_publication.publish()
        # Set the publication year to the previous year
        first_publication.publication_date = current_date.replace(year=current_date.year - 1)
        first_publication.save()

        second_publication = Magazine.objects.get(pk=2)
        second_publication.publish()

        self.assertEqual(second_publication.volume, first_publication.volume + 1)
        self.assertEqual(second_publication.issue, 1)
