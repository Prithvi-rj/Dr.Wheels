# Generated by Django 5.0.3 on 2024-04-04 09:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebGuest', '0004_alter_tbl_shop_shop_photo_alter_tbl_shop_shop_proof_and_more'),
        ('WebOwner', '0008_initial'),
        ('WebWorkShop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_requestserviceowner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_message', models.CharField(max_length=500)),
                ('request_postdate', models.DateField(auto_now_add=True)),
                ('request_status', models.IntegerField(default='0')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebGuest.tbl_boatowner')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebWorkShop.tbl_service')),
            ],
        ),
    ]
