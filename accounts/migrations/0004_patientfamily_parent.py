# Generated by Django 4.2.7 on 2024-06-01 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0003_patient_create_date_patient_is_examined"),
    ]

    operations = [
        migrations.AddField(
            model_name="patientfamily",
            name="parent",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="accounts.patient",
            ),
        ),
    ]
