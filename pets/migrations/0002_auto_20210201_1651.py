# Generated by Django 3.1.4 on 2021-02-01 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='color',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='type',
            name='type_of_animal',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
