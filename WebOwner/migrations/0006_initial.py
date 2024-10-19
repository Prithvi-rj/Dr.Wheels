# Generated by Django 5.0.3 on 2024-03-30 12:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('WebAdmin', '0003_tbl_boattype'),
        ('WebGuest', '0004_alter_tbl_shop_shop_photo_alter_tbl_shop_shop_proof_and_more'),
        ('WebOwner', '0005_delete_tbl_boatdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_boatdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boat_name', models.CharField(max_length=50)),
                ('boat_details', models.CharField(max_length=500)),
                ('boat_rate', models.CharField(max_length=500)),
                ('boat_photo', models.FileField(upload_to='Assets/BoatPhoto/')),
                ('boat_proof', models.FileField(upload_to='Assets/BoatProof/')),
                ('boattype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebAdmin.tbl_boattype')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebGuest.tbl_boatowner')),
            ],
        ),
    ]
