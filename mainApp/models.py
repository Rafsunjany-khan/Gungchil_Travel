from django.db import models

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

class Travel(models.Model):
    travelDate = models.DateField()
    departure = models.CharField(max_length=20, choices=CITY, default='')
    destination = models.CharField(max_length=20, choices=CITY)
    busNo = models.ForeignKey(Bus, on_delete=models.CASCADE)
    timeSchedule = models.CharField(max_length=100)
    distance = models.IntegerField()

    def price(self):
        return self.distance * 2.3

class Booked(models.Model):
    name = models.CharField(max_length=200)
    busNo = models.ForeignKey(Travel, on_delete=models.CASCADE)
    time = models.CharField(max_length=100)
    issue = models.BooleanField()


class Notice(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=200)
    notice = models.TextField()
