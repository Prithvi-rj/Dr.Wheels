# Generated by Django 5.0.3 on 2024-03-30 12:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAdmin', '0003_tbl_boattype'),
        ('WebOwner', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_boatdetails',
            name='owner',
        ),
        migrations.AlterField(
            model_name='tbl_boatdetails',
            name='boattype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebAdmin.tbl_boattype'),
        ),
    ]