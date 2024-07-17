# Generated by Django 4.2.7 on 2024-06-02 12:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0007_rename_emp_email_doctor_doc_email_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="doctor",
            name="doc_email",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to=settings.AUTH_USER_MODEL,
                verbose_name="doctor",
            ),
        ),
    ]
