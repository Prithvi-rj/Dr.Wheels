# Generated by Django 5.0.3 on 2024-03-30 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAdmin', '0002_tbl_brand_tbl_servicetype'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_boattype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boattype_name', models.CharField(max_length=50)),
            ],
        ),
    ]
