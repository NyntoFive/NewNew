from django.core.management.base import BaseCommand
import re
import json


class Command(BaseCommand):
    help = "My shiny new management command."

    def add_arguments(self, parser):
        parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        def clean_description(txt):
            return txt.replace('\r\n\t','\n').replace('\t','')
        def clean_image_urls(txt):
            return re.findall(r"https://www.knifekits.com/vcom/images/\S+\.jpg", txt)
        
        raise NotImplementedError()
