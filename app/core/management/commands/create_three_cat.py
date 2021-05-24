from django.core.management.base import BaseCommand
from core.models import Cat


class Command(BaseCommand):
    help = 'Commando to create three new cats'

    def handle(self, *args, **options):
        cat1 = Cat.objects.create(
            breeed='Persian Cat',
            location_of_origin='Iran',
            coat_length='long',
            body_type='cobby',
            pattern='solid bi-color tabby calic'
        )
        cat2 = Cat.objects.create(
            breeed='British Cat',
            location_of_origin='Great Britain',
            coat_length='short',
            body_type='semi-cobby',
            pattern='solid bi-color tabby'
        )
        cat3 = Cat.objects.create(
            breeed='Brasilian Cat',
            location_of_origin='Brasil',
            coat_length='short',
            body_type='semi-cobby',
            pattern='solid bi-color tabby'
        )
        cat1.save()
        cat2.save()
        cat3.save()

        self.stdout.write(self.style.SUCCESS(
            'Create three new breed cats in database!'))
