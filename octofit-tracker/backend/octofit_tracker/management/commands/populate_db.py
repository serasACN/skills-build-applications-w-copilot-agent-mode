from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete all data
        # Borrar en orden de dependencias para evitar errores de claves primarias
            # Las colecciones ya se limpiaron con mongosh, no borrar desde Django

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel team')
        dc = Team.objects.create(name='DC', description='DC team')

        # Users
        users = [
            User.objects.create(name='Spiderman', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Ironman', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
        ]

        # Workouts
        cardio = Workout.objects.create(name='Cardio', description='Run fast')
        strength = Workout.objects.create(name='Strength', description='Lift heavy')
        cardio.suggested_for.add(marvel, dc)
        strength.suggested_for.add(marvel, dc)

        # Activities
        Activity.objects.create(user=users[0], type='run', duration=30, date='2025-11-17')
        Activity.objects.create(user=users[1], type='cycle', duration=45, date='2025-11-16')
        Activity.objects.create(user=users[2], type='swim', duration=25, date='2025-11-15')
        Activity.objects.create(user=users[3], type='lift', duration=60, date='2025-11-14')

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=200)
        Leaderboard.objects.create(team=dc, points=180)

        # El índice único en email se debe crear con mongosh, no desde Django

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
