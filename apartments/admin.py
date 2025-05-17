from django.contrib import admin
from .models import Apartment, Note, Address, Activities, PointsOfInterests, Comments
# Register your models here.
admin.site.register(Apartment)
admin.site.register(Note)
admin.site.register(Address)
admin.site.register(Activities)
admin.site.register(PointsOfInterests)
admin.site.register(Comments)