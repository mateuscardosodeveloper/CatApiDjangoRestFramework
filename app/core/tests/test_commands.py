from django.test import TestCase
from django.core.management import call_command
from core.models import Cat


class CommandsTestCase(TestCase):

    def test_to_create_three_new_cats(self):
        """Test to create three new cats"""
        call_command('create_three_cat')
        cat = Cat.objects.all().order_by('breeed')

        self.assertEqual(len(cat), 3)
