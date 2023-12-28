from django.contrib import admin
from .models import Bus,Travel, Booked, City, Issued, Seat

# List display admin page for Bus table
class BusAdmin(admin.ModelAdmin):
    list_display = ['busNo','busType','color']

class TravelAdmin(admin.ModelAdmin):
    list_display = ['pnrNo','busNo','departure','destination','timeSchedule']

class BookedAdmin(admin.ModelAdmin):
    list_display = ['customerPnr', 'name', 'pnrNo','departure','destination','total_price', 'busNo']

class CityAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Bus, BusAdmin)
admin.site.register(Travel, TravelAdmin)
admin.site.register(Booked, BookedAdmin)
admin.site.register(City, CityAdmin)

admin.site.register(Issued)
admin.site.register(Seat)