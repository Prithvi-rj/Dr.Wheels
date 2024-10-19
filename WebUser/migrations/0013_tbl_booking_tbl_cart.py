# Generated by Django 5.0.3 on 2024-04-03 11:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebGuest', '0004_alter_tbl_shop_shop_photo_alter_tbl_shop_shop_proof_and_more'),
        ('WebShop', '0003_tbl_product_product_stock'),
        ('WebUser', '0012_remove_tbl_cart_booking_remove_tbl_cart_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_status', models.IntegerField(default=0)),
                ('booking_amount', models.CharField(max_length=30)),
                ('boking_date', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='WebGuest.tbl_boatowner')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='WebGuest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_qty', models.IntegerField(default=1)),
                ('cart_status', models.IntegerField(default=0)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebUser.tbl_booking')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebShop.tbl_product')),
            ],
        ),
    ]
