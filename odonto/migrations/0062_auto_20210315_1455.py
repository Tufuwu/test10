# Generated by Django 2.0.13 on 2021-03-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odonto', '0061_auto_20210315_1125'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='covidstatus',
            options={'verbose_name': 'COVID-19 status', 'verbose_name_plural': 'COVID-19 statuses'},
        ),
        migrations.AlterModelOptions(
            name='covidtriage',
            options={'verbose_name': 'COVID-19 triage'},
        ),
        migrations.AlterField(
            model_name='covidstatus',
            name='other_covid_status',
            field=models.IntegerField(blank=True, null=True, verbose_name='Other COVID-19 status'),
        ),
        migrations.AlterField(
            model_name='covidtriage',
            name='covid_status',
            field=models.CharField(blank=True, choices=[('Patient is shielded', 'Patient is shielded'), ('Increased risk of illness from COVID-19', 'Increased risk of illness from COVID-19'), ('Possible/confirmed COVID-19 patient (or those living in household)', 'Possible/confirmed COVID-19 patient (or those living in household)'), ('Other', 'Other'), ('Patient is COVID-19 symptom free at present', 'Patient is COVID-19 symptom free at present')], max_length=256, null=True, verbose_name='COVID-19 status'),
        ),
    ]
