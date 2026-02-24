from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Users
        users = [
            User(email='ironman@marvel.com', name='Iron Man', team='Marvel', super_power='Genius'),
            User(email='spiderman@marvel.com', name='Spider-Man', team='Marvel', super_power='Spider Sense'),
            User(email='batman@dc.com', name='Batman', team='DC', super_power='Detective'),
            User(email='wonderwoman@dc.com', name='Wonder Woman', team='DC', super_power='Strength'),
        ]
        for user in users:
            user.save()

        # Activities
        Activity.objects.create(user='Iron Man', activity_type='Running', duration=30, date='2026-02-24')
        Activity.objects.create(user='Spider-Man', activity_type='Jumping', duration=15, date='2026-02-24')
        Activity.objects.create(user='Batman', activity_type='Cycling', duration=45, date='2026-02-24')
        Activity.objects.create(user='Wonder Woman', activity_type='Swimming', duration=60, date='2026-02-24')

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity workout for heroes', difficulty='Hard')
        Workout.objects.create(name='Sidekick Stretch', description='Stretching routine for sidekicks', difficulty='Easy')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
