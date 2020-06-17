# Generated by Django 3.0.6 on 2020-06-09 19:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Time of Creation'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ads',
            name='vendor_name',
            field=models.CharField(choices=[('Kinda Home', 'Kinda Home'), ('Inovia', 'Inovia'), ('Casacon', 'Casacon'), ('NCR Angola', 'NCR Angola'), ('Seaside', 'Seaside'), ('Soba-store', 'Soba-store'), ('Megáfrica', 'Megáfrica'), ('Maxi', 'Maxi'), ('Meu Merkado', 'Meu Merkado')], default=1, max_length=100, verbose_name='Vendor Name'),
        ),
    ]