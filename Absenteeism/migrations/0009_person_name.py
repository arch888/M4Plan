# Generated by Django 2.0 on 2018-06-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Absenteeism', '0008_auto_20180628_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
