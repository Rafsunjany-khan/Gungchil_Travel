import random
import string
from django.db import models
from multiselectfield import MultiSelectField


BUS_TYPE =(
    ('i10', 'i10'),
    ('Double Dacker', 'Double Dacker'),
    ('D45i', 'D44i'),
)
class Bus(models.Model):
    busNo = models.CharField(max_length=100)
    busType = models.CharField(max_length=20, choices=BUS_TYPE, default='i10')
    registrationNo = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    details = models.TextField()

    def __str__(self):
        return self.busNo

class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Issued(models.Model):
    name = models.CharField(max_length=255, default='Self')

    def __str__(self):
        return self.name

def pnr_generate_bus():
    source = string.digits + string.ascii_letters
    result_str = ''.join((random.choice(source) for i in range(6)))
    return result_str

class Travel(models.Model):
    travelDate = models.DateField()
    departure = models.ForeignKey(City, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(City, on_delete=models.CASCADE, related_name='destinations')
    busNo = models.ForeignKey(Bus, on_delete=models.CASCADE)
    timeSchedule = models.CharField(max_length=100)
    distance = models.IntegerField()
    pnrNo = models.CharField(max_length=100, unique=True, null=True, blank=True)
    price = models.FloatField(default=False)

    def save(self, *args, **kwargs):
        self.pnrNo = pnr_generate_bus()
        super(Travel, self).save(*args, **kwargs)
    #def price(self):
        #return self.distance * 2.3

    def __str__(self):
        return self.pnrNo


class Notice(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=200)
    notice = models.TextField()

class Seat(models.Model):
    seat_No = models.CharField(max_length=10)

    def __str__(self):
        return self.seat_No


def pnr_generate():
    source = string.ascii_uppercase + string.digits
    result_str = ''.join((random.choice(source) for i in range(6)))
    return result_str

class Booked(models.Model):
    ticketNo = models.AutoField(primary_key=True)
    customerPnr = models.CharField(max_length=100, unique=True, null=True)
    pnrNo = models.CharField(max_length=100)
    busNo = models.CharField(max_length=100, null=True)
    issuedBy = models.CharField(max_length=100)
    issueDate = models.DateTimeField(auto_now_add=True)
    issueFrom = models.CharField(max_length=100, null=True)
    travelDate = models.CharField(max_length=100, null=False)
    timeSchedule = models.CharField(max_length=100, default='')
    departure = models.CharField(max_length=100, null=False, default='')
    destination = models.CharField(max_length=100, null=False, default='')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contactNo = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    seatNo = models.CharField(max_length=100)
    price = models.CharField(max_length=20, null=True)
    total_price = models.DecimalField(max_digits=20, decimal_places=2, null=True)
    def save(self, *args, **kwargs):
        self.customerPnr = pnr_generate()
        super(Booked, self).save(*args, **kwargs)

    def totalPrice(self, *args, **kwargs):
        total_seat = Booked.objects.all(self.seatNo).count()
        self.total_price = self.price * total_seat
        super(Booked, self).save(*args, **kwargs)
