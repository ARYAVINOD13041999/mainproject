# Generated by Django 4.1.4 on 2023-02-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('momo_app', '0004_add_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('startingtime', models.TimeField()),
                ('endingtime', models.TimeField()),
            ],
        ),
    ]