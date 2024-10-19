# Generated by Django 5.0.3 on 2024-03-30 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebGuest', '0003_tbl_shop_tbl_workshop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_shop',
            name='shop_photo',
            field=models.FileField(upload_to='Assets/ShopPhoto/'),
        ),
        migrations.AlterField(
            model_name='tbl_shop',
            name='shop_proof',
            field=models.FileField(upload_to='Assets/ShopProof/'),
        ),
        migrations.AlterField(
            model_name='tbl_workshop',
            name='workshop_photo',
            field=models.FileField(upload_to='Assets/WorkShopPhoto/'),
        ),
        migrations.AlterField(
            model_name='tbl_workshop',
            name='workshop_proof',
            field=models.FileField(upload_to='Assets/WorkShopProof/'),
        ),
    ]
