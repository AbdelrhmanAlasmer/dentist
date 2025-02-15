# Generated by Django 4.2.7 on 2024-06-07 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("visits", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Xray",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "xray_photo",
                    models.ImageField(blank=True, null=True, upload_to="xray/%Y/%m/%d"),
                ),
                ("xray_url", models.URLField()),
                (
                    "visit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="visits.visit"
                    ),
                ),
            ],
        ),
    ]
