# Generated by Django 4.0.5 on 2024-01-17 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flipkart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_image', models.ImageField(upload_to='uploads/category/')),
                ('category_name', models.CharField(default='', max_length=100, null=True)),
            ],
        ),
    ]
