# Generated by Django 4.2 on 2023-11-20 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0005_alter_preference_countries_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification_name', models.CharField(max_length=255)),
                ('year_of_certification', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certifications', to='job_application.registration')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_of_passing', models.IntegerField()),
                ('school', models.CharField(max_length=255)),
                ('degree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_application.degree')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='job_application.registration')),
            ],
        ),
        migrations.AlterField(
            model_name='preference',
            name='countries',
            field=models.ManyToManyField(blank=True, to='job_application.country'),
        ),
        migrations.AlterField(
            model_name='preference',
            name='industries',
            field=models.ManyToManyField(blank=True, to='job_application.industry'),
        ),
        migrations.DeleteModel(
            name='EducationCertification',
        ),
    ]