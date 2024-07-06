from django.contrib import admin
from homepage.models import place_type, place, user, Cart



# Register your models here.
admin.site.register(place_type)
admin.site.register(place)
class placeAdmin(admin.ModelAdmin):
    list_display=['place_type','place_name','image']
admin.site.register(user)
admin.site.register(Cart)

