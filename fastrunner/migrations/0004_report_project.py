# Generated by Django 2.1.3 on 2018-12-07 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fastrunner', '0003_auto_20181207_1452'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='project',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='fastrunner.Project'),
            preserve_default=False,
        ),
    ]
