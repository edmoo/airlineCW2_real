# Generated by Django 4.2.1 on 2023-05-06 14:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=10)),
                ('terminals', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('price', models.FloatField()),
                ('insurance', models.BooleanField()),
                ('status', models.CharField(max_length=50)),
                ('start_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('plane_type', models.CharField(max_length=50)),
                ('number_of_seats', models.IntegerField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='airline_api.airport')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='airline_api.airport')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('seat_class', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('name', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FlightSeat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline_api.flight')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline_api.seat')),
            ],
        ),
        migrations.AddField(
            model_name='flight',
            name='seats',
            field=models.ManyToManyField(through='airline_api.FlightSeat', to='airline_api.seat'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('luggage', models.IntegerField()),
                ('passport', models.IntegerField()),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='airline_api.booking')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline_api.seat')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='airline_api.customer'),
        ),
        migrations.AddField(
            model_name='booking',
            name='flight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airline_api.flight'),
        ),
    ]