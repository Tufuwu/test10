# Generated by Django 2.2.10 on 2020-04-01 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('errata', '0041_auto_20200326_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailtext',
            name='email_case',
            field=models.CharField(blank=True, choices=[('Created in Fall', 'Created in Fall'), ('Created in Spring', 'Created in Spring'), ('Reviewed and (will not fix, or duplicate, or not an error, or major book revision)', 'Reviewed and (will not fix, or duplicate, or not an error, or major book revision)'), ('Reviewed and Approved', 'Reviewed and Approved'), ('Completed and Sent to Customer Support', 'Completed and Sent to Customer Support'), ('More Information Requested', 'More Information Requested'), ('Getting New Edition', 'Getting New Edition'), ('Partner Product', 'Partner Product'), ('Generic Completed Response', 'Generic Completed Response')], max_length=100, null=True),
        ),
    ]
