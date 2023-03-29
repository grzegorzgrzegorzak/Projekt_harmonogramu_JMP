# Create your tests here.
from datetime import timedelta

from models import *

from django.test import TestCase
from django.test.utils import override_settings
from django.utils import timezone
import freezegun


@freezegun.freeze_time('2022-06-01 10:00:00', tick=True)
def test_my_model_queryset(self):
    my_model = Store.objects.all()

