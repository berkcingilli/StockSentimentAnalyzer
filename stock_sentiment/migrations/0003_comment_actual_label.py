# Generated by Django 3.1.5 on 2021-02-04 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_sentiment', '0002_exceptions'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='actual_label',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
