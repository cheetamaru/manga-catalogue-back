# Generated by Django 4.1.3 on 2022-11-16 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_mangatitle_authors_mangatitle_chaptercount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mangatitle',
            name='endDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='mangatitle',
            name='startDate',
            field=models.DateField(null=True),
        ),
    ]
