from django.contrib import admin
from .models import Bus,Travel, Booked

# List display admin page for Bus table
class BusAdmin(admin.ModelAdmin):
    list_display = ['busNo','busType','color']

class TravelAdmin(admin.ModelAdmin):
    list_display = ['pnrNo','travelDate','busNo','departure','destination','timeSchedule']

class BookedAdmin(admin.ModelAdmin):
    list_display = ['pnrNo','name','issueDate']

admin.site.register(Bus, BusAdmin)
admin.site.register(Travel, TravelAdmin)
admin.site.register(Booked, BookedAdmin)