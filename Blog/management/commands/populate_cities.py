import csv
from django.core.management.base import BaseCommand
from Blog.models import Cities

class Command(BaseCommand):
    help = 'Populate the Cities table from a CSV file'

    def handle(self, *args, **kwargs):
        with open('/Users/radek/Desktop/Project-6/BlogisekJPN/japanBlog/Blog/management/commands/import.csv',encoding='ISO-8859-1', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip the header row
            for row in reader:
                name, description, image_url = row
                #if len(row) == 3:
                    
                #else:
                #    print(f"Skipping row with unexpected number of columns: {row}")
                city, created = Cities.objects.get_or_create(
                    name=name,
                    defaults={'description': description, 'image_url': image_url }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully added {name}'))
                else:
                    self.stdout.write(f'{name} already exists')
