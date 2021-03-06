# Generated by Django 2.0 on 2018-07-13 07:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Approver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approve', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_grp', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FactoryMerchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factory_mrchant', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PDMerchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pd_mrchant', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProductionMerchant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_mrchant', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pch', models.CharField(max_length=10)),
                ('style', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=2500)),
                ('sketch', models.FileField(upload_to='static/images')),
            ],
        ),
        migrations.CreateModel(
            name='Stylemaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('item_group', models.CharField(max_length=100)),
                ('season', models.CharField(blank=True, max_length=100, null=True)),
                ('responsible', models.CharField(max_length=100)),
                ('product_designer', models.CharField(blank=True, max_length=100, null=True)),
                ('sales_person', models.CharField(max_length=100)),
                ('basic_uom', models.CharField(max_length=100)),
                ('alt_uom', models.CharField(blank=True, max_length=100, null=True)),
                ('conversion_factor', models.CharField(blank=True, max_length=100, null=True)),
                ('currency', models.CharField(max_length=100)),
                ('sales_price', models.CharField(max_length=100)),
                ('sale_price_qty', models.CharField(blank=True, max_length=100, null=True)),
                ('buying_house_commission', models.CharField(blank=True, max_length=100, null=True)),
                ('licence', models.CharField(blank=True, max_length=100, null=True)),
                ('national_dbk', models.DecimalField(blank=True, decimal_places=4, default=0, max_digits=7, null=True)),
                ('rosl_group', models.CharField(blank=True, max_length=100, null=True)),
                ('propertys', models.CharField(blank=True, max_length=100, null=True)),
                ('order_confirmation_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Date')),
                ('pcd', models.DateField(blank=True, null=True)),
                ('ex_factory_date', models.DateField(blank=True, null=True)),
                ('approver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stylemaster.Approver')),
                ('custom_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stylemaster.CustomGroup')),
                ('factory_merchant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stylemaster.FactoryMerchant')),
                ('item_no', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stylemaster.Sample')),
                ('pd_merchant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stylemaster.PDMerchant')),
                ('production_merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stylemaster.ProductionMerchant')),
            ],
        ),
    ]
