# Generated by Django 2.2.5 on 2019-09-14 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20190914_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='originator',
            name='pesel',
            field=models.BigIntegerField(verbose_name='PESEL'),
        ),
    ]
