# Generated by Django 2.0.7 on 2018-08-09 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('absenteeism', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select', models.CharField(choices=[('LINE-1', 'LINE-1'), ('LINE-2', 'LINE-2'), ('LINE-3', 'LINE-3'), ('LINE-4', 'LINE-4'), ('LINE-5', 'LINE-5')], max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='choose',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='absenteeism.Lining'),
            preserve_default=False,
        ),
    ]
