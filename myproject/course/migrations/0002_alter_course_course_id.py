# Generated by Django 4.2.16 on 2024-11-26 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="course_id",
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
