# Generated by Django 4.2.3 on 2023-10-09 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("poesias", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="username",
            field=models.CharField(max_length=50, unique=True),
        )
    ]