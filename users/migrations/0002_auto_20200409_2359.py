# Generated by Django 3.0.5 on 2020-04-09 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("users", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ("name", "email"),
                "verbose_name": "user",
                "verbose_name_plural": "users",
            },
        ),
        migrations.RemoveField(model_name="user", name="username"),
    ]
