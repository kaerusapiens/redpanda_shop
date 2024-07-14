# Generated by Django 5.0.6 on 2024-07-14 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('slug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_description', models.TextField(blank=True)),
                ('product_image', models.ImageField(upload_to='')),
                ('can_return', models.BooleanField(default=True)),
                ('est_ship_date', models.CharField(choices=[('In Stock', 'in_stock'), ('Drop Ship', 'drop_ship')], default='In Stock', max_length=10)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='store.category')),
            ],
        ),
    ]
