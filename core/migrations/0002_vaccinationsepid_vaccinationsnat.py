# Generated by Django 3.0.8 on 2022-10-26 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VaccinationsNat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_vac', models.TextField(blank=True)),
                ('second_vac', models.TextField(blank=True)),
                ('third_vac', models.TextField(blank=True)),
                ('third_risk', models.TextField(blank=True)),
                ('fourth_risk', models.TextField(blank=True)),
                ('first_revac', models.TextField(blank=True)),
                ('second_revac', models.TextField(blank=True)),
                ('third_revac', models.TextField(blank=True)),
                ('vaccination', models.TextField(blank=True)),
                ('revaccination', models.TextField(blank=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Vaccinations')),
            ],
            options={
                'verbose_name': 'Прививка нацкалендарь',
                'verbose_name_plural': 'Прививки нацкалендарь',
            },
        ),
        migrations.CreateModel(
            name='VaccinationsEpid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Vaccinations')),
            ],
            options={
                'verbose_name': 'Прививка по эпидпоказаниям',
                'verbose_name_plural': 'Прививки по эпидпоказаниям',
            },
        ),
    ]
