# Generated by Django 3.0.5 on 2020-04-30 03:10

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Region",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "code",
                    models.CharField(
                        help_text="Required. At most 30 characters. Prioritize official code from government or geographic institution.",
                        max_length=30,
                        verbose_name="code",
                    ),
                ),
                (
                    "parent_hierarchy",
                    models.CharField(
                        blank=True,
                        help_text='At most 180 characters. Identifier to simplify filtering. Set each level as the region code, separated by ":" character.',
                        max_length=180,
                        null=True,
                        verbose_name="Default parent hierarchy",
                    ),
                ),
                (
                    "kind",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (0, "None"),
                            (1, "World"),
                            (2, "Continent"),
                            (3, "Country"),
                            (4, "Macroregion"),
                            (5, "State"),
                            (6, "Mesoregion"),
                            (7, "City"),
                            (8, "Neighborhood"),
                        ],
                        default=0,
                        help_text="Required. The region type according to the hierarchy of geographic regions.",
                        verbose_name="type",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Required. At most 150 characters.",
                        max_length=150,
                        verbose_name="name",
                    ),
                ),
                (
                    "abbr",
                    models.CharField(
                        blank=True,
                        help_text="At most 100 characters.",
                        max_length=100,
                        verbose_name="name abbreviation",
                    ),
                ),
                (
                    "lat",
                    models.DecimalField(
                        blank=True,
                        decimal_places=7,
                        help_text="Required. Must be a float number between -90 and 90, inclusive, with maximum precision of seven digits.",
                        max_digits=9,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("-90.0")),
                            django.core.validators.MaxValueValidator(Decimal("90.0")),
                        ],
                        verbose_name="latitude",
                    ),
                ),
                (
                    "lng",
                    models.DecimalField(
                        blank=True,
                        decimal_places=7,
                        help_text="Required. Must be a float number between -180 and 180, inclusive, with maximum precision of seven digits.",
                        max_digits=10,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("-180.0")),
                            django.core.validators.MaxValueValidator(Decimal("180.0")),
                        ],
                        verbose_name="longitude",
                    ),
                ),
                (
                    "parents",
                    models.ManyToManyField(
                        help_text="Each region from which is part.",
                        related_name="children",
                        to="hcap_geo.Region",
                        verbose_name="Parent regions",
                    ),
                ),
            ],
            options={
                "verbose_name": "region",
                "verbose_name_plural": "regions",
                "ordering": ("kind", "parent_hierarchy", "abbr"),
                "permissions": (("fill", "Can add regions to database"),),
                "unique_together": {("kind", "parent_hierarchy", "code")},
            },
        ),
    ]
