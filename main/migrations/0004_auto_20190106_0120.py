# Generated by Django 2.1.4 on 2019-01-06 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("main", "0003_analytic")]

    operations = [
        migrations.AlterField(
            model_name="candidacy",
            name="party",
            field=models.CharField(blank=True, max_length=300, null=True),
        )
    ]
