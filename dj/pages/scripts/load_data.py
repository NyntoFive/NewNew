import json
from datetime import timedelta
from django.utils import timezone

from pages.models import DJItem

def load_file(file="recents.json"):
    with open(file) as f:
        data = json.load(f)
    return data


def run(*args):

    # Fetch all DJItems
    items = DJItem.objects.all()
    if 'staleonly' in args:
        # Only get items more than 14 days old...
        items = items.filter(created__lt=timezone.now() - timedelta(days=-14))