# Generated by Django 4.2 on 2023-11-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0003_alter_preference_has_passport_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name_plural': 'Countries'},
        ),
        migrations.AlterModelOptions(
            name='degree',
            options={'verbose_name_plural': 'Degrees'},
        ),
        migrations.AlterModelOptions(
            name='industry',
            options={'verbose_name_plural': 'Industries'},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name_plural': 'Skills'},
        ),
        migrations.AlterModelOptions(
            name='state',
            options={'verbose_name_plural': 'States'},
        ),
        migrations.RemoveField(
            model_name='preference',
            name='countries',
        ),
        migrations.RemoveField(
            model_name='preference',
            name='industries',
        ),
        migrations.AddField(
            model_name='preference',
            name='countries',
            field=models.ManyToManyField(to='job_application.country'),
        ),
        migrations.AddField(
            model_name='preference',
            name='industries',
            field=models.ManyToManyField(to='job_application.industry'),
        ),
    ]
