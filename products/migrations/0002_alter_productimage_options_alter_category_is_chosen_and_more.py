# Generated by Django 4.2.3 on 2023-07-28 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="productimage",
            options={
                "ordering": ["id"],
                "verbose_name": "изображение товара",
                "verbose_name_plural": "изображения товаров",
            },
        ),
        migrations.AlterField(
            model_name="category",
            name="is_chosen",
            field=models.BooleanField(default=False, verbose_name="избранная"),
        ),
        migrations.AlterField(
            model_name="category",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="удалена"),
        ),
        migrations.AlterField(
            model_name="product",
            name="created",
            field=models.DateTimeField(auto_now_add=True, verbose_name="создан"),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, verbose_name="описание"),
        ),
        migrations.AlterField(
            model_name="product",
            name="features",
            field=models.JSONField(
                blank=True, null=True, verbose_name="характеристики"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated",
            field=models.DateTimeField(auto_now=True, verbose_name="обновлён"),
        ),
        migrations.AlterField(
            model_name="productimage",
            name="title",
            field=models.CharField(max_length=512, verbose_name="название изображения"),
        ),
        migrations.AddIndex(
            model_name="productimage",
            index=models.Index(fields=["id"], name="products_pr_id_456e59_idx"),
        ),
    ]
