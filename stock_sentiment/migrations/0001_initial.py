# Generated by Django 3.1.5 on 2021-02-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(blank=True, max_length=200, null=True)),
                ('ticker_symbol', models.CharField(blank=True, max_length=200, null=True)),
                ('original_comment', models.TextField(blank=True, null=True)),
                ('pre_processed_comment', models.TextField(blank=True, null=True)),
                ('comment_date', models.DateTimeField()),
                ('pos', models.FloatField(blank=True, null=True)),
                ('neu', models.FloatField(blank=True, null=True)),
                ('neg', models.FloatField(blank=True, null=True)),
                ('compound', models.FloatField(blank=True, null=True)),
                ('label', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
