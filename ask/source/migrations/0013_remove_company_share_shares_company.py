# Generated by Django 4.0.3 on 2022-03-31 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0012_alter_company_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='share',
        ),
        migrations.AddField(
            model_name='shares',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='source.company'),
        ),
    ]
