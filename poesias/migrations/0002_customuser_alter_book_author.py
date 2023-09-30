# Generated by Django 4.2.3 on 2023-09-30 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("poesias", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
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
                ("email", models.EmailField(max_length=255, unique=True)),
                ("password", models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="poesias.author",
            ),
        ),
    ]
