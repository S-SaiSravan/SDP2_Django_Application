# Generated by Django 4.0.3 on 2022-04-30 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_project_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='budget',
            field=models.IntegerField(null=True),
        ),
    ]
