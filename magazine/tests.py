from django.test import TestCase

from .models import Magazine

from .utils import int_to_roman

from datetime import date


class MagazineTestCase(TestCase):
    def setUp(self):
        Magazine.objects.create()
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

        third_publication = Magazine.objects.get(pk=3)
        third_publication.publish()

        self.assertEqual(second_publication.volume, first_publication.volume)
        self.assertEqual(second_publication.issue, first_publication.volume + 1)

        self.assertEqual(third_publication.volume, second_publication.volume)
        self.assertEqual(third_publication.issue, second_publication.issue + 1)

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

    def test_publish_changes_nothing_if_published(self):
        """Publishing a published magazine changes nothing"""
        publication = Magazine.objects.get(pk=1)
        publication.publish()

        initial_volume = publication.volume
        initial_issue = publication.issue
        initial_publication_date = publication.publication_date

        publication.publish()

        self.assertEqual(publication.volume, initial_volume)
        self.assertEqual(publication.issue, initial_issue)
        self.assertEqual(publication.publication_date, initial_publication_date)
        self.assertEqual(publication.status, 'p')

    def test_publish_changes_only_status_if_withdrawn(self):
        """Publishing a withdrawn magazine only updates its status"""
        publication = Magazine.objects.get(pk=1)
        publication.publish()
        publication.withdraw()

        initial_volume = publication.volume
        initial_issue = publication.issue
        initial_publication_date = publication.publication_date

        publication.publish()

        self.assertEqual(publication.volume, initial_volume)
        self.assertEqual(publication.issue, initial_issue)
        self.assertEqual(publication.publication_date, initial_publication_date)
        self.assertEqual(publication.status, 'p')
    
    def test_withdraw_changes_status_if_published(self):
        """Withdrawing a published magazine sets the status to withdrawn"""
        publication = Magazine.objects.get(pk=1)
        publication.publish()
        
        self.assertEqual(publication.status, 'p')
        publication.withdraw()
        self.assertEqual(publication.status, 'w')


    def test_withdraw_changes_nothing_if_draft(self):
        """Drafts may not be withdrawn"""
        publication = Magazine.objects.get(pk=1)
        
        self.assertEqual(publication.status, 'd')
        publication.withdraw()
        self.assertEqual(publication.status, 'd')


class UtilsTestCase(TestCase):
    def test_int_to_roman(self):
        """Function should convert integers to roman numerals correctly"""
        self.assertEqual(int_to_roman(1), 'I')
        self.assertEqual(int_to_roman(2), 'II')
        self.assertEqual(int_to_roman(3), 'III')
        self.assertEqual(int_to_roman(4), 'IV')
        self.assertEqual(int_to_roman(5), 'V')
        self.assertEqual(int_to_roman(6), 'VI')
        self.assertEqual(int_to_roman(7), 'VII')
        self.assertEqual(int_to_roman(8), 'VIII')
        self.assertEqual(int_to_roman(9), 'IX')
        self.assertEqual(int_to_roman(10), 'X')
        # random sample of [1, 10000] from random.org
        self.assertEqual(int_to_roman(7022), 'MMMMMMMXXII')
        self.assertEqual(int_to_roman(9939), 'MMMMMMMMMCMXXXIX')
        self.assertEqual(int_to_roman(115), 'CXV')
        self.assertEqual(int_to_roman(6627), 'MMMMMMDCXXVII')
        self.assertEqual(int_to_roman(5692), 'MMMMMDCXCII')
