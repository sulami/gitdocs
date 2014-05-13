from django.core.management.base import BaseCommand
from processor.models import Docs
from datetime import date

class Command(BaseCommand):
    help = 'Deletes Docs older than 7 days from cache'

    def handle(self, *args, **options):
        count = 0
        for d in Docs.objects.all():
            if (date.today() - d.time).days >= 8:
                d.delete()
        print 'Deleted {} docs'.format(count)

