# Generated by Django 4.1.3 on 2022-11-18 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_mangatitle_firstcoverimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mangatitle',
            name='status',
            field=models.CharField(choices=[('finished', 'Finished'), ('ongoing', 'Publishing'), ('hiatus', 'On Hiatus'), ('canceled', 'Discontinued'), ('notstarted', 'Not Yet Published')], max_length=12, null=True),
        ),
    ]