from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Squirrel(models.Model):

	latitude = models.FloatField(
		help_text='latitude',
		)

	longitude = models.FloatField(
		help_text='longitude',
		)

	unique_squirrel_id = models.CharField(
		help_text='unique_squirrel_id',
		max_length=32,
		)
	AM='am'
	PM='pm'
	shift = models.CharField(
		help_text='shift',
		max_length=16,
		choices=(
			(AM,'AM'),
			(PM,'PM'),
			),
		)

	date = models.DateField(
		help_text='date',
		)
	Adult='adult'
	Juvenile='juvenile'
	age_choice=(
		(Adult,"Adult"),
		(Juvenile,"Juvenile"),
		)
	age = models.CharField(
		help_text='age',
		max_length=16,
		choices=age_choice,
		)

	Gray='gray'
	Black='black'
	Cinnamon='cinnamon'
	primary_fur_color_choice=(
		(Gray,'Gray'),
		(Black,'Black'),
		(Cinnamon,'Cinnamon'),
		)
	primary_fur_color=models.CharField(
		help_text='primary fur color',
		max_length=30,
		choices=primary_fur_color_choice,
		)

	Ground_Plane='ground plane'
	Above_Ground='above ground'
	location_choice=(
		(Ground_Plane,'Ground Plan'),
		(Above_Ground,'Above Ground'),
		)
	location=models.CharField(
		help_text='location',
		max_length=100,
		choices=location_choice,
		)

	specific_location=models.CharField(
		help_text='specific_location',
                max_length=100,
		)

	running=models.BooleanField(
		help_text='running',
		)

	chasing=models.BooleanField(
		help_text='chasing',
		)

	climbing=models.BooleanField(
		help_text='climbing',
		)

	eating=models.BooleanField(
		help_text='eating',
		)

	foraging=models.BooleanField(
		help_text='foraging',
		)

	other_activities=models.CharField(
		help_text='other_activities',
                max_length=100,
		)

	kuks=models.BooleanField(
		help_text='kuks',
		)

	quaas=models.BooleanField(
		help_text='quaas',
		)

	moans=models.BooleanField(
		help_text='moans',
		)

	tail_flags=models.BooleanField(
		help_text='tail_flags',
		)

	tail_twitches=models.BooleanField(
		help_text='tail_twitches',
		)

	approaches=models.BooleanField(
		help_text='approaches',
		)

	indifferent=models.BooleanField(
		help_text='indifferent',
		)

	runs_from=models.BooleanField(
		help_text='runs from',
		)
	
	def __str__(self):
		return self.unique_squirrel_id

	

