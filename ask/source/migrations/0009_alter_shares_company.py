# Generated by Django 4.0.3 on 2022-03-28 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0008_shares_share_display_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shares',
            name='company',
            field=models.CharField(max_length=255, null=True),
        ),
    ]