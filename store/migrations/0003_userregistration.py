# Generated by Django 5.1.3 on 2024-12-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_catogary_product_delete_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
