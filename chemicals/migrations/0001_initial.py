# Generated by Django 4.0.4 on 2022-08-17 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InChi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inchi', models.CharField(max_length=511, verbose_name='InChi')),
                ('inchi_key', models.CharField(max_length=27, unique=True, verbose_name='InChiKey')),
                ('mw', models.FloatField(verbose_name='Molecular Weight (g/mol)')),
            ],
            options={
                'verbose_name': 'InChi',
                'verbose_name_plural': 'InChi',
            },
        ),
        migrations.CreateModel(
            name='SMILES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smiles', models.CharField(max_length=511)),
                ('inchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chemicals.inchi')),
            ],
            options={
                'verbose_name': 'SMILES',
                'verbose_name_plural': 'SMILES',
            },
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=511)),
                ('iupac', models.BooleanField(default=False, verbose_name='IUPAC')),
                ('common_name', models.BooleanField(default=False)),
                ('abbreviation', models.BooleanField(default=False)),
                ('inchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inchi_name', to='chemicals.inchi')),
            ],
            options={
                'verbose_name': 'Name',
                'verbose_name_plural': 'Names',
            },
        ),
        migrations.CreateModel(
            name='CAS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cas', models.CharField(max_length=31)),
                ('inchi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inchi_cas', to='chemicals.inchi')),
            ],
            options={
                'verbose_name': 'CAS',
                'verbose_name_plural': 'CAS',
            },
        ),
    ]
