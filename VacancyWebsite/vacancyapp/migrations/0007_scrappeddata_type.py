# Generated by Django 3.1.7 on 2021-04-04 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancyapp', '0006_scrappeddata_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrappeddata',
            name='type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]