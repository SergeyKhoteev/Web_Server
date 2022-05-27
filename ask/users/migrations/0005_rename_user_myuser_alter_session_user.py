# Generated by Django 4.0.2 on 2022-05-26 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0019_alter_question_rating'),
        ('users', '0004_alter_user_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='MyUser',
        ),
        migrations.AlterField(
            model_name='session',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.myuser'),
        ),
    ]