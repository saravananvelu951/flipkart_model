# Generated by Django 4.0.5 on 2024-01-23 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0004_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='quatity',
            new_name='quantity',
        ),
    ]