from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Model, CharField, IntegerField, DateTimeField, \
    OneToOneField, ForeignKey, SET_NULL



# Create your models here.

class StoreType(Model):
    condition = CharField(max_length=30)

    # class Meta:
    #     app_label = 'dfafasdfasdf'


class Supervisor(Model):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Region(Model):
    name = CharField(max_length=30)


class Subcontractor(Model):
    name = CharField(max_length=30)
    contact_person = CharField(max_length=30)
    phone_number = CharField(max_length=9)

    def __str__(self):
        return self.name


class Store(Model):
    REGION = (
        ('T','Wojnicz'),
        ('LUB','Lubartów')
    )

    store_number = CharField(max_length=4, null=False)
    store_city = CharField(max_length=30)
    store_street = CharField(max_length=30)
    store_street_number = CharField(max_length=30)
    zip_code = CharField(max_length=6)
    date_start_installation = DateTimeField(null=True)
    date_opening = DateTimeField(null=True)
    date_disassembling = DateTimeField(null=True)
    store_type = ForeignKey(StoreType, null=True, on_delete=SET_NULL)
    supervisor = ForeignKey(Supervisor, null=True, on_delete=SET_NULL)
    region = ForeignKey(Region, null=True, on_delete=SET_NULL, choices=REGION)
    subcontractor = ForeignKey(Subcontractor, null=True, on_delete=SET_NULL)

    class Meta:
        app_label = "schedule"

    def __str__(self):
        return f"{self.store_number} {self.store_city} {self.store_street}"

    "Jak zrobić aby w zależności od tego czy jest typ nowy, date disassemblin się nie pojawiała"


class MaterialConfiguration(Model):
    pass

