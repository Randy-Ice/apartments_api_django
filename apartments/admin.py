from django.contrib import admin
from .models import Apartment, Note, Address, Activities, PointsOfInterests, Comments
# Register your models here.






@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'address','number_of_beds',  'baths', 'pets_allowed',
                    'price','home_type',  'contact']
    list_editable = ['pets_allowed', 'price', 'contact']
    list_per_page = 10
    list_filter = ['number_of_beds', 'baths', 'pets_allowed', 'home_type']
    autocomplete_fields = ['activities', 'points_of_interests', 'address']

@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 10

@admin.register(PointsOfInterests)
class PointsOfInterestsAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_per_page = 10

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['location']
    search_fields = ['location']


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['apartment', 'description']

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = [
        'apartment', 'name',  'description', 'created_at']





