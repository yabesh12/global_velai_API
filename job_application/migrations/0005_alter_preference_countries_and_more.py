# Generated by Django 4.2 on 2023-11-20 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0004_alter_country_options_alter_degree_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preference',
            name='countries',
            field=models.ManyToManyField(blank=True, null=True, to='job_application.country'),
        ),
        migrations.AlterField(
            model_name='preference',
            name='industries',
            field=models.ManyToManyField(blank=True, null=True, to='job_application.industry'),
        ),
    ]
