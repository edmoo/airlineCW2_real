# Generated by Django 4.2.1 on 2023-05-11 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline_api', '0014_alter_airport_id_alter_booking_id_alter_customer_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='available',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
