# Generated by Django 2.2.4 on 2019-08-26 10:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0017_auto_20190825_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='ident',
            field=models.UUIDField(default=uuid.UUID('75727e77-28f5-4c7b-9dcf-8cb6880ffb5e'), editable=False, primary_key=True, serialize=False),
        ),
    ]