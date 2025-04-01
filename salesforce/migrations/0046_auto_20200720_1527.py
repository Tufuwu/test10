# Generated by Django 3.0.4 on 2020-07-20 20:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20200720_1527'),
        ('salesforce', '0045_auto_20200707_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceDownload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_format', models.CharField(blank=True, choices=[('Online', 'Online'), ('PDF', 'PDF'), ('Print', 'Print'), ('App', 'App'), ('Kindle', 'Kindle'), ('iBooks', 'iBooks'), ('Bookshare', 'Bookshare'), ('Chegg Reader', 'Chegg Reader')], max_length=100, null=True)),
                ('account_id', models.IntegerField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_access', models.DateTimeField(auto_now=True)),
                ('number_of_times_accessed', models.IntegerField()),
                ('resource_name', models.CharField(max_length=255)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.Book')),
            ],
        ),
        migrations.AddIndex(
            model_name='resourcedownload',
            index=models.Index(fields=['account_id'], name='salesforce__account_b11d37_idx'),
        ),
        migrations.AddIndex(
            model_name='resourcedownload',
            index=models.Index(fields=['book'], name='salesforce__book_id_971691_idx'),
        ),
    ]
