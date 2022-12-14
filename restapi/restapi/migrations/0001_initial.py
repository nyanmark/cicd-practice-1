# Generated by Django 4.1.1 on 2022-09-24 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PastDegreesToRadiansResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seconds_input', models.DecimalField(decimal_places=8, max_digits=10)),
                ('minutes_input', models.DecimalField(decimal_places=8, max_digits=10)),
                ('degress_input', models.DecimalField(decimal_places=8, max_digits=10)),
                ('radians_output', models.DecimalField(decimal_places=8, max_digits=10)),
            ],
        ),
    ]
