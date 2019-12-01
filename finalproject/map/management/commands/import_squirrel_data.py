from django.core.management.base import BaseCommand, CommandError
from squirrels.models import Squirrel

class Command(BaseCommand):
    help = 'import the squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):
        for path in options['path']:
            f = open('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv', 'r')
            for line in f:
                args = line.split(',')
                if args[0] != 'X':
                    longitude = args[0]
                    latitude = args[1]
                    unique_id = args[2]
                    shift=args[4]
                    date=args[5][4:]+'-'+args[5][:2]+'+'+args[5][2:4]
                    age =args[7]
                    primary_fur_color=args[8]
                    location=args[12]
                    specific_location=args[14]
                    running=args[15]
                    chasing=args[16]
                    climbing=args[17]
                    eating=args[18]
                    foraging=args[19]
                    other_activities=args[20]
                    kuks=args[21]
                    quaas=args[22]
                    moans=args[23]
                    tail_flags=args[24]
                    tail_twitches=args[25]
                    approaches=args[26]
                    indifferent=args[27]
                    runs_from=args[28]

                    Squirrel.objects.create(
                        latitude=latitude, 
                        longitude=longitude,
                        unique_squirrel_id=unique_id,
                        shift=shift,
                        date=date,
                        age=age,
                        primary_fur_color=primary_fur_color,
                        location=location,
                        specific_location=specific_location,
                        running=running,
                        chasing=chasing,
                        climbing=climbing,
                        eating=eating,
                        foraging=foraging,
                        other_activities=other_activities,
                        kuks=kuks,
                        quaas=quaas,
                        moans=moans,
                        tail_twitches=tail_twitches,
                        tail_flags=tail_flags,
                        approaches=approaches,
                        indifferent=indifferent,
                        runs_from=runs_from
                        )

