# Generated by Django 4.0.2 on 2022-03-07 07:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qa', '0007_question_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='autor',
        ),
        migrations.AddField(
            model_name='question',
            name='auhtor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
    ]