# Generated by Django 2.2.5 on 2019-09-14 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0015_auto_20190914_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Uwagi'),
        ),
    ]
