from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.models import Cat


CAT_URL = reverse('cat:cat-list')


def sample_cat(
    breeed='Persian',
    location_of_origin='Iran',
    coat_length='long',
    body_type='cobby',
    pattern='solid bi-color tabby calic'
):
    """Create a sample cat"""

    return Cat.objects.create(
        breeed=breeed,
        location_of_origin=location_of_origin,
        coat_length=coat_length,
        body_type=body_type,
        pattern=pattern,
    )


def detail_url(cat_id):
    """detail cat url"""
    return reverse('cat:cat-detail', args=[cat_id])


class PrivateCatApiTests(TestCase):
    """Test private objects in cats"""

    def setUp(self):
        self.client = APIClient()

    def test_create_new_cat_successful(self):
        """Test to create a new cat success"""
        payload = {
            'breeed': 'Persian Cat',
            'location_of_origin': 'Iran',
            'coat_length': 'long',
            'body_type': 'cobby',
            'pattern': 'solid bi-color tabby calic',
        }
        response = self.client.post(CAT_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_new_cat_failed(self):
        """Test to create a new cat failed"""
        payload = {
            'breeed': '',
            'location_of_origin': 'Iran',
            'coat_length': 'long',
            'body_type': 'cobby',
            'pattern': 'solid bi-color tabby calic',
        }
        response = self.client.post(CAT_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_partial_update_cat(self):
        """Test to update partial object cat"""
        cat = sample_cat()
        payload = {'breeed': 'British Cat'}

        url = detail_url(cat.id)
        response = self.client.patch(url, payload)

        cat.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(cat.breeed, payload['breeed'])

    def test_full_update_cat(self):
        """Test to full update cat objects"""
        cat = sample_cat()
        payload = {
            'breeed': 'British Cat',
            'location_of_origin': 'Great Britain',
            'coat_length': 'short',
            'body_type': 'semi-cobby',
            'pattern': 'solid bi-color tabby'
        }

        url = detail_url(cat.id)
        response = self.client.put(url, payload)

        cat.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(cat.breeed, payload['breeed'])
        self.assertEqual(cat.location_of_origin, payload['location_of_origin'])
        self.assertEqual(cat.coat_length, payload['coat_length'])
        self.assertEqual(cat.body_type, payload['body_type'])
        self.assertEqual(cat.pattern, payload['pattern'])

    def test_breeed_is_unique_value(self):
        """Test to check if breed is unique value"""
        cat1 = sample_cat()
        cat2 = Cat.objects.create(
            breeed='British Cat',
            location_of_origin='Great Britain',
            coat_length='short',
            body_type='semi-cobby',
            pattern='solid bi-color tabby'
        )
        payload = {
            'breeed': 'British Cat',
        }

        url = detail_url(cat1.id)
        response = self.client.patch(url, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(cat2.breeed, payload['breeed'])
        self.assertRaisesMessage(
            ValueError, 'cat with this breeed already exists.')

    def test_filter_negative_value_search(self):
        """Test when filter with negative value return null"""
        sample_cat()
        sample_cat(breeed='Brasilian Cat')

        inner_qs = Cat.objects.filter(breeed__contains='British Cat').values(
            'breeed',
            'location_of_origin',
            'coat_length',
            'body_type',
            'pattern',
        )

        self.assertEqual(len(inner_qs), 0)
