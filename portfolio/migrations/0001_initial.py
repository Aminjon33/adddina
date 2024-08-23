# Generated by Django 5.0.8 on 2024-08-23 04:06

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('client', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.portfoliocategory')),
            ],
        ),
    ]