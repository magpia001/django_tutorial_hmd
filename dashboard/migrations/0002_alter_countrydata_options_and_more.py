# Generated by Django 4.1.7 on 2023-03-29 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='countrydata',
            options={'verbose_name_plural': '각 나라별 인구데이터'},
        ),
        migrations.AlterField(
            model_name='countrydata',
            name='population',
            field=models.FloatField(),
        ),
    ]
