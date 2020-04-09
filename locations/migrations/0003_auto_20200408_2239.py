# Generated by Django 3.0.5 on 2020-04-08 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_fill_states_and_cities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipality',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='locations.State'),
        ),
    ]
