import uuid

from django.core.validators import MinLengthValidator
from django.db import models
from django.conf import settings
# Create your models here.

class Apartment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100,
                            validators=[MinLengthValidator(3)]
                            )
    description = models.TextField(
        validators=[MinLengthValidator(10)]
    )
    image = models.ImageField(null=True,blank=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    BED_ONE = "1 bed"
    BED_TWO = "2 beds"
    BED_THREE = "3 beds"
    BED_FOUR = "4 beds"
    BED_OPTIONS = [
        (BED_ONE, "1 bed"),
        (BED_TWO, "2 beds"),
        (BED_THREE, "3 beds"),
        (BED_FOUR, "4 beds"),
    ]
    number_of_beds = models.CharField(max_length=10, choices=BED_OPTIONS, default=BED_ONE)
    BATH_1 = "1 bath"
    BATH_2 = "2 baths"
    BATH_3 = "3 baths"
    BATH_OPTIONS = [
        (BATH_1, '1 bath'),
        (BATH_2, '2 baths'),
        (BATH_3, '3 baths'),
    ]
    baths = models.CharField(max_length=10, choices=BATH_OPTIONS, default=BATH_1)

    PET_YES = "y"
    PET_NO = "n"
    PET_OPTIONS = [
        (PET_YES, "yes"),
        (PET_NO, "no"),
    ]
    pets_allowed = models.CharField(max_length=10, choices=PET_OPTIONS, default=PET_NO)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    APARTMENT = 'Apartment'
    STUDIO = 'Studio'
    TYPES_OPTIONS = [
        (APARTMENT, 'Apartment'),
        (STUDIO, 'Studio'),
    ]
    home_type = models.CharField(max_length=10, choices=TYPES_OPTIONS, default=APARTMENT)
    square_feet = models.TextField(max_length=255, validators=[MinLengthValidator(3)])
    contact = models.TextField(max_length=255, validators=[MinLengthValidator(3)])
    activities = models.ManyToManyField('Activities', blank=True)
    points_of_interests = models.ManyToManyField('PointsOfInterests', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.name} {self.description}"

    class Meta:
        ordering = ['name']



class Note(models.Model):
    apartment = models.OneToOneField(Apartment, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField()

    def __str__(self):
        return self.apartment.name + ' ' + self.description

class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.CharField(max_length=255)
    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']

class Activities(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class PointsOfInterests(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True,
                            validators=[MinLengthValidator(3)]
                            )
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Comments(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{str(self.name.username)} {self.apartment.name}"

    class Meta:
        ordering = ['created_at']