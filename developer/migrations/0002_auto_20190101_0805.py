# Generated by Django 2.1.3 on 2019-01-01 08:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('developer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='app',
            name='secret',
            field=models.CharField(blank=True, max_length=100, verbose_name='application secret'),
        ),
        migrations.AlterField(
            model_name='app',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='apps', to=settings.AUTH_USER_MODEL),
        ),
    ]
