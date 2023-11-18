import random
import string
from django.db import models
from multiselectfield import MultiSelectField


BUS_TYPE =(
    ('i10', 'i10'),
    ('Double Dacker', 'Double Dacker'),
    ('D45i', 'D44i'),
)
CITY =(
    ('Bogura', 'Bogura'),
    ('Dhaka', 'Dhaka'),
    ('Dinajpur', 'Dinajpur'),
    ('Rajshahi', 'Rajshahi'),
    ('Rangpur', 'Rangpur'),
    ('Pabna', 'Pabna'),
    ('Kustia', 'Kustia'),
)

class Bus(models.Model):
    busNo = models.CharField(max_length=100)
    busType = models.CharField(max_length=20, choices=BUS_TYPE, default='i10')
    registrationNo = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    details = models.TextField()

    def __str__(self):
        return self.busNo

def pnr_generate_bus():
    source = string.digits + string.ascii_letters
    result_str = ''.join((random.choice(source) for i in range(6)))
    return result_str

class Travel(models.Model):
    travelDate = models.DateField()
    departure = models.CharField(max_length=20, choices=CITY, default='')
    destination = models.CharField(max_length=20, choices=CITY)
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



class Notice(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=200)
    notice = models.TextField()

def pnr_generate():
    source = string.ascii_uppercase + string.digits
    result_str = ''.join((random.choice(source) for i in range(6)))
    return result_str

class Booked(models.Model):
    SEAT = (
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('A3', 'A3'),
        ('A4', 'A4'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('B3', 'B3'),
        ('B4', 'B4'),
    )
    CounterMember = (
        ('Hasan Ali', 'Hasan Ali'),
        ('Emran', 'Emran'),
        ('Torikul', 'Torikul'),
    )
    ticketNo = models.AutoField(primary_key=True)
    pnrNo = models.CharField(max_length=100, unique=True, null=True, blank=True)
    issuedBy = models.CharField(choices=CounterMember, max_length=100)
    issueDate = models.DateTimeField(auto_now_add=True)
    issueFrom = models.CharField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contactNo = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    busNo = models.ForeignKey(Travel, on_delete=models.CASCADE)
    seatNo = MultiSelectField(max_length=255, choices=SEAT)

    def save(self, *args, **kwargs):
        self.pnrNo = pnr_generate()
        super(Booked, self).save(*args, **kwargs)