# Generated by Django 4.1.1 on 2022-09-24 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0005_alter_pastdegreestoradiansresult_degress_result_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastdegreestoradiansresult',
            name='radians_output',
            field=models.DecimalField(decimal_places=12, max_digits=14),
        ),
    ]
