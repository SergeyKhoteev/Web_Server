# Generated by Django 4.0.3 on 2022-03-18 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IndexComposition',
            new_name='ETF_Structure',
        ),
        migrations.RenameModel(
            old_name='MarketIndexes',
            new_name='ETFs',
        ),
    ]
