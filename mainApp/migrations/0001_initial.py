# Generated by Django 4.2.5 on 2023-11-05 17:49

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('busNo', models.CharField(max_length=100)),
                ('busType', models.CharField(choices=[('i10', 'i10'), ('Double Dacker', 'Double Dacker'), ('D45i', 'D44i')], default='i10', max_length=20)),
                ('registrationNo', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=200)),
                ('notice', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('travelDate', models.DateField()),
                ('departure', models.CharField(choices=[('Bogura', 'Bogura'), ('Dhaka', 'Dhaka'), ('Dinajpur', 'Dinajpur'), ('Rajshahi', 'Rajshahi'), ('Rangpur', 'Rangpur'), ('Pabna', 'Pabna'), ('Kustia', 'Kustia')], default='', max_length=20)),
                ('destination', models.CharField(choices=[('Bogura', 'Bogura'), ('Dhaka', 'Dhaka'), ('Dinajpur', 'Dinajpur'), ('Rajshahi', 'Rajshahi'), ('Rangpur', 'Rangpur'), ('Pabna', 'Pabna'), ('Kustia', 'Kustia')], max_length=20)),
                ('timeSchedule', models.CharField(max_length=100)),
                ('distance', models.IntegerField()),
                ('busNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.bus')),
            ],
        ),
        migrations.CreateModel(
            name='Booked',
            fields=[
                ('ticketNo', models.AutoField(primary_key=True, serialize=False)),
                ('pnrNo', models.CharField(max_length=100)),
                ('issuedBy', models.CharField(choices=[('Hasan Ali', 'Hasan Ali'), ('Emran', 'Emran'), ('Torikul', 'Torikul')], max_length=100)),
                ('issueDate', models.DateField()),
                ('issueFrom', models.CharField()),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('contactNo', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('seatNo', multiselectfield.db.fields.MultiSelectField(choices=[('A1', 'A1'), ('A2', 'A2'), ('A3', 'A3'), ('A4', 'A4'), ('B1', 'B1'), ('B2', 'B2'), ('B3', 'B3'), ('B4', 'B4')], max_length=255)),
                ('busNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.travel')),
            ],
        ),
    ]
