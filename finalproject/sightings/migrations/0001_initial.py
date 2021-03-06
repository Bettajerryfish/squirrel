# Generated by Django 2.2.7 on 2019-12-06 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sightings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(help_text='latitude')),
                ('longitude', models.FloatField(help_text='longitude')),
                ('unique_squirrel_id', models.CharField(help_text='unique_squirrel_id', max_length=32)),
                ('shift', models.CharField(choices=[('am', 'AM'), ('pm', 'PM')], help_text='shift', max_length=16)),
                ('date', models.DateField(help_text='date')),
                ('age', models.CharField(choices=[('adult', 'Adult'), ('juvenile', 'Juvenile')], help_text='age', max_length=16)),
                ('primary_fur_color', models.CharField(choices=[('gray', 'Gray'), ('black', 'Black'), ('cinnamon', 'Cinnamon')], help_text='primary fur color', max_length=30)),
                ('location', models.CharField(choices=[('ground plane', 'Ground Plan'), ('above ground', 'Above Ground')], help_text='location', max_length=100)),
                ('specific_location', models.CharField(help_text='specific_location', max_length=100)),
                ('running', models.BooleanField(blank=True, help_text='running', null=True)),
                ('chasing', models.BooleanField(blank=True, help_text='chasing', null=True)),
                ('climbing', models.BooleanField(blank=True, help_text='climbing', null=True)),
                ('eating', models.BooleanField(blank=True, help_text='eating', null=True)),
                ('foraging', models.BooleanField(blank=True, help_text='foraging', null=True)),
                ('other_activities', models.CharField(help_text='other_activities', max_length=100)),
                ('kuks', models.BooleanField(blank=True, help_text='kuks', null=True)),
                ('quaas', models.BooleanField(blank=True, help_text='quaas', null=True)),
                ('moans', models.BooleanField(blank=True, help_text='moans', null=True)),
                ('tail_flags', models.BooleanField(blank=True, help_text='tail_flags', null=True)),
                ('tail_twitches', models.BooleanField(blank=True, help_text='tail_twitches', null=True)),
                ('approaches', models.BooleanField(blank=True, help_text='approaches', null=True)),
                ('indifferent', models.BooleanField(blank=True, help_text='indifferent', null=True)),
                ('runs_from', models.BooleanField(blank=True, help_text='runs from', null=True)),
            ],
        ),
    ]
