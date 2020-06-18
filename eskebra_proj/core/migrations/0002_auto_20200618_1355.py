# Generated by Django 3.0.6 on 2020-06-18 13:55

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='ads',
            name='unique_ads',
        ),
        migrations.AddConstraint(
            model_name='ads',
            constraint=models.CheckConstraint(check=models.Q(price__gt=django.db.models.expressions.F('disc_price')), name='check_prices'),
        ),
    ]