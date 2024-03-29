# Generated by Django 2.0 on 2019-03-10 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fitness', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField(verbose_name='Start Time')),
                ('end_time', models.TimeField(verbose_name='End Time')),
                ('created_on', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='logDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_sets', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('weight_used', models.DecimalField(decimal_places=1, max_digits=4)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitness.workout')),
                ('parent_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='log.log')),
            ],
        ),
    ]
