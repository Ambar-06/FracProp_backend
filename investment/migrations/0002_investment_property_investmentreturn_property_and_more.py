# Generated by Django 5.1.3 on 2025-01-22 07:48

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("investment", "0001_initial"),
        ("property", "0002_property_investment_lock_in_period_in_months_and_more"),
        ("user", "0002_alter_user_options_alter_user_unique_together_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="investment",
            name="property",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="investments",
                to="property.property",
            ),
        ),
        migrations.AddField(
            model_name="investmentreturn",
            name="property",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="property_returns",
                to="property.property",
            ),
        ),
        migrations.AddField(
            model_name="investmentreturn",
            name="return_type",
            field=models.CharField(
                choices=[("RENTAL", "rental"), ("VALUATION", "valuation")],
                default="RENTAL",
                max_length=255,
                null=True,
            ),
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, db_index=True, null=True),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("meta", models.JSONField(blank=True, null=True)),
                (
                    "uuid",
                    models.UUIDField(db_index=True, default=uuid.uuid4, unique=True),
                ),
                ("is_deleted", models.BooleanField(db_index=True, default=False)),
                ("amount", models.FloatField(null=True)),
                (
                    "type",
                    models.CharField(
                        choices=[("DEPOSIT", "deposit"), ("WITHDRAWAL", "withdrawal")],
                        default="DEPOSIT",
                        max_length=255,
                        null=True,
                    ),
                ),
                ("remarks", models.TextField(blank=True, null=True)),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="user.user",
                    ),
                ),
            ],
            options={
                "get_latest_by": "updated_at",
                "abstract": False,
            },
        ),
    ]
