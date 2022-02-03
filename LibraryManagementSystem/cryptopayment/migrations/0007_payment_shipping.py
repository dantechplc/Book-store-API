# Generated by Django 3.1.5 on 2021-02-05 19:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("commercebackend", "0011_auto_20210205_1949"),
        ("cryptopayment", "0006_payment_total_price_btc"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="shipping",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="commercebackend.shippingmodel",
            ),
            preserve_default=False,
        ),
    ]
