# Generated by Django 4.0.3 on 2022-04-30 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_subject_project_descr'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
    ]