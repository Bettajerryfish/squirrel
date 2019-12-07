import csv
from map.models import Squirrel
from django.core.management import BaseCommand
from django.utils.encoding import smart_str
class Command(BaseCommand):
    help = 'Export the data'
    def add_arguments(self, parser):
        parser.add_argument('positionArg')
    def handle(self,*args,**kargs):
        path=kargs['positionArg']
        with open(path, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow([
                smart_str(u"Unique_Squirrel_ID"),
                smart_str(u"Longitude"),
                smart_str(u"Latitude"),
                smart_str(u"Shift"),
                smart_str(u"Date"),
                smart_str(u"Age"),
                smart_str(u"Primary_fur_color"),
                smart_str(u"Location"),
                smart_str(u"Specific_location"),
                smart_str(u"Running"),
                smart_str(u"Chasing"),
                smart_str(u"Climbing"),
                smart_str(u"Eating"),
                smart_str(u"Foraging"),
                smart_str(u"Other_Activities"),
                smart_str(u"Kuks"),
                smart_str(u"Quaas"),
                smart_str(u"Moans"),
                smart_str(u"Tail_flags"),
                smart_str(u"Tail_twitches"),
                smart_str(u"Approaches"),
                smart_str(u"Indifferent"),
                smart_str(u"Runs_from"),    
                ])
            for obj in Squirrel.objects.values():
                spamwriter.writerow([
                    smart_str(obj['unique_squirrel_id']),
                    smart_str(obj["longitude"]),
                    smart_str(obj["latitude"]),
                    smart_str(obj["shift"]),
                    smart_str(obj["date"]),
                    smart_str(obj["age"]),
                    smart_str(obj["primary_fur_color"]),
                    smart_str(obj["location"]),
                    smart_str(obj["specific_location"]),
                    smart_str(obj["running"]),
                    smart_str(obj["chasing"]),
                    smart_str(obj["climbing"]),
                    smart_str(obj["eating"]),
                    smart_str(obj["foraging"]),
                    smart_str(obj["other_activities"]),
                    smart_str(obj["kuks"]),
                    smart_str(obj["quaas"]),
                    smart_str(obj["moans"]),
                    smart_str(obj["tail_flags"]),
                    smart_str(obj["tail_twitches"]),
                    smart_str(obj["approaches"]),
                    smart_str(obj["indifferent"]),
                    smart_str(obj["runs_from"]),])
