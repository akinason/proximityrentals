# Generated by Django 2.1.3 on 2018-12-02 13:30

from django.db import migrations, models
import main.defaults


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20181202_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='phone number'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, default=main.defaults.get_default_username, max_length=100, unique=True, verbose_name='username'),
        ),
    ]
