# Generated by Django 4.2.5 on 2023-09-25 17:55

from django.db import migrations, models
import django.db.models.deletion


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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=100)),
                ('issue', models.BooleanField()),
                ('busNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.travel')),
            ],
        ),
    ]