# Django
from django.core.management.base import BaseCommand

# local Django
from apps.user.database.seeders import UserSeed

class Command(BaseCommand):

  def handle(self, *args, **options):

    UserSeed()