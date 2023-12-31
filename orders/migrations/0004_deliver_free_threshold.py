# Generated by Django 4.2.3 on 2023-09-07 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0003_alter_order_client"),
    ]

    operations = [
        migrations.AddField(
            model_name="deliver",
            name="free_threshold",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="порог бесплатной доставки",
            ),
        ),
    ]
