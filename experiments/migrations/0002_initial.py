# Generated by Django 4.0.4 on 2022-08-17 01:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experiments', '0001_initial'),
        ('chemicals', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reactor',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.group'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='experiments.company'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.group'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='inchi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='getInventory', to='chemicals.inchi'),
        ),
        migrations.AddField(
            model_name='experiment_chemicals',
            name='experiment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='experiments.experiment'),
        ),
        migrations.AddField(
            model_name='experiment_chemicals',
            name='inventory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='getExperiments', to='experiments.inventory'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='reactor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='experiments.reactor'),
        ),
        migrations.AddField(
            model_name='experiment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
