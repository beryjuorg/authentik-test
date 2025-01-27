# Generated by Django 3.2.8 on 2021-10-14 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_stages_authenticator_sms", "0003_auto_20211014_0813"),
    ]

    operations = [
        migrations.AlterField(
            model_name="authenticatorsmsstage",
            name="auth_type",
            field=models.TextField(
                choices=[("basic", "Basic"), ("bearer", "Bearer")], default="basic"
            ),
        ),
        migrations.AlterField(
            model_name="authenticatorsmsstage",
            name="auth_password",
            field=models.TextField(blank=True, default=""),
        ),
    ]
