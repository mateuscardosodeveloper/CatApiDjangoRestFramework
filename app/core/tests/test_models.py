from django.test import TestCase

from core import models


class ModelsTests(TestCase):

    def test_create_cat_str(self):
        """Test create cat with string representation"""
        cat = models.Cat.objects.create(
            breeed='Persian',
            location_of_origin='Iran',
            coat_length='long',
            body_type='cobby',
            pattern='solid bi-color tabby calic'
        )

        self.assertEqual(str(cat), cat.breeed)
