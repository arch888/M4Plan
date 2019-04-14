# Generated by Django 2.0 on 2018-07-19 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Department'),
        ),
        migrations.AlterField(
            model_name='person',
            name='fab',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Fabric'),
        ),
        migrations.AlterField(
            model_name='person',
            name='sect',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Sections'),
        ),
        migrations.AlterField(
            model_name='person',
            name='subsect',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Subsection'),
        ),
        migrations.AlterField(
            model_name='person',
            name='was',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='category.Wash'),
        ),
    ]