# Generated by Django 4.1.3 on 2022-11-18 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_mangatitle_enddate_mangatitle_startdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mangatitle',
            name='firstCoverImage',
            field=models.ImageField(blank=True, null=True, upload_to='base/uploads/covers'),
        ),
    ]
