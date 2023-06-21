# Generated by Django 4.1.7 on 2023-04-01 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vsetaq', '0005_goals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='expenses',
            field=models.DecimalField(decimal_places=2, max_digits=50),
        ),
        migrations.AlterField(
            model_name='expenses',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='goals',
            name='save_money',
            field=models.DecimalField(decimal_places=2, max_digits=50),
        ),
        migrations.AlterField(
            model_name='goals',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='income',
            field=models.DecimalField(decimal_places=2, max_digits=50),
        ),
    ]