# Generated by Django 4.2.3 on 2023-08-17 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0009_action"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="action",
            name="products_ac_created_e5d98d_idx",
        ),
        migrations.RemoveIndex(
            model_name="action",
            name="products_ac_target__57e28c_idx",
        ),
    ]
