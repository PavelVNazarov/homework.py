# Generated by Django 3.2.25 on 2024-12-24 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('url', models.CharField(max_length=100)),
                ('short_name', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('balance', models.IntegerField()),
                ('email', models.TextField(max_length=100)),
            ],
        ),
    ]
