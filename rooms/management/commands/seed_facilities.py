from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "This command to create facilities"
    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times", help="How many times do you wanna me to tell you that I love you?"
    #         )

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on permises",
            "Paid parking off permises",
            "Elevator",
            "Parking",
            "Gym"
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f'{len(facilities)} facilites created!!'))
