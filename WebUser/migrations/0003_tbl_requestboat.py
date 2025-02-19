# Generated by Django 5.0.3 on 2024-03-30 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebGuest', '0004_alter_tbl_shop_shop_photo_alter_tbl_shop_shop_proof_and_more'),
        ('WebUser', '0002_tbl_requestservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_requestboat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_message', models.CharField(max_length=500)),
                ('request_todate', models.CharField(max_length=500, null=True)),
                ('request_postdate', models.DateField(auto_now_add=True)),
                ('request_status', models.IntegerField(default='0')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebGuest.tbl_user')),
            ],
        ),
    ]
