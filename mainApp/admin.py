from django.contrib import admin
from .models import Bus,Travel

# List display admin page for Bus table
class BusAdmin(admin.ModelAdmin):
    list_display = ['busNo','busType','color']

class TravelAdmin(admin.ModelAdmin):
    list_display = ['travelDate','busNo','departure','destination','timeSchedule']


admin.site.register(Bus, BusAdmin)
admin.site.register(Travel, TravelAdmin)