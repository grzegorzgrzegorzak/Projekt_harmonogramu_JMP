from datetime import datetime, timedelta

from django.test import TestCase

# Create your tests here.
from models import *


def test_in30days_query(date: datetime.date):
    return Store.objects.filter(date_opening__gte=date,
                                date_opening__lt=date
                                                 + timedelta(days=30))

assert test_in30days_query(datetime.date(2022, 6, 1))