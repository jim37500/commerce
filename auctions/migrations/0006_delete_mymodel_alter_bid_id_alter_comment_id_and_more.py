# Generated by Django 4.2.7 on 2023-11-08 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_mymodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
        migrations.AlterField(
            model_name='bid',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='listing',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]