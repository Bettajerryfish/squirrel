# Generated by Django 2.2.7 on 2019-12-06 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='approaches',
            field=models.BooleanField(blank=True, help_text='approaches', null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='chasing',
            field=models.BooleanField(blank=True, help_text='chasing', null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='climbing',
            field=models.BooleanField(blank=True, help_text='climbing', null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='eating',
            field=models.BooleanField(blank=True, help_text='eating', null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='foraging',
            field=models.BooleanField(blank=True, help_text='foraging', null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='indifferent',
            field=models.BooleanField(blank=True, help_text='indifferent', null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='kuks',
            field=models.BooleanField(blank=True, help_text='kuks', null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='moans',
            field=models.BooleanField(blank=True, help_text='moans', null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='quaas',
            field=models.BooleanField(blank=True, help_text='quaas', null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='running',
            field=models.BooleanField(blank=True, help_text='running', null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='runs_from',
            field=models.BooleanField(blank=True, help_text='runs from', null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='tail_flags',
            field=models.BooleanField(blank=True, help_text='tail_flags', null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='tail_twitches',
            field=models.BooleanField(blank=True, help_text='tail_twitches', null=True),
        ),
    ]