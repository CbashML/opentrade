# Generated by Django 2.2.4 on 2019-08-25 08:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0012_auto_20190825_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='ident',
            field=models.UUIDField(default=uuid.UUID('469a892f-dd30-46ca-913e-818ed31653bd'), editable=False, primary_key=True, serialize=False),
        ),
    ]