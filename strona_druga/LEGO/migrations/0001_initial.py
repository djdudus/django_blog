# Generated by Django 4.1.8 on 2023-06-12 13:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brick_number', models.CharField(max_length=20)),
                ('color_id', models.CharField(max_length=10)),
                ('category_id', models.IntegerField()),
                ('type', models.CharField(max_length=15)),
                ('min_price', models.FloatField()),
                ('avg_price', models.FloatField()),
                ('max_price', models.FloatField()),
                ('notes', models.TextField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('set_number', models.CharField(max_length=10, unique=True)),
                ('min_price', models.FloatField()),
                ('avg_price', models.FloatField()),
                ('max_price', models.FloatField()),
                ('brickprice', models.FloatField()),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='SetBricks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brick_number', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('set_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='LEGO.set')),
            ],
        ),
    ]
