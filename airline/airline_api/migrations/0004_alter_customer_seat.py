# Generated by Django 4.2.1 on 2023-05-07 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airline_api', '0003_alter_customer_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='seat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='airline_api.seat'),
        ),
    ]