# Generated by Django 2.0 on 2018-09-20 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='jupyter_url',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
