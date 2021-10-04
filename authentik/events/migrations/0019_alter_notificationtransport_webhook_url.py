# Generated by Django 3.2.7 on 2021-10-04 15:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_events", "0018_auto_20210911_2217"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notificationtransport",
            name="webhook_url",
            field=models.TextField(blank=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]