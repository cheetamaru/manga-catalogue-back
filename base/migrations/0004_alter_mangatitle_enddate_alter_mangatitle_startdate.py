# Generated by Django 4.1.3 on 2022-11-16 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_mangatitle_enddate_alter_mangatitle_startdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mangatitle',
            name='endDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='mangatitle',
            name='startDate',
            field=models.DateTimeField(null=True),
        ),
    ]