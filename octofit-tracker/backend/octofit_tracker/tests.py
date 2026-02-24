from django.test import TestCase
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email='test@hero.com', name='Test Hero', team='Marvel', super_power='Testing')
        self.assertEqual(user.email, 'test@hero.com')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team', description='Test Desc')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user='Test Hero', activity_type='Testing', duration=10, date='2026-02-24')
        self.assertEqual(activity.activity_type, 'Testing')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team='Test Team', points=50)
        self.assertEqual(lb.points, 50)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Desc', difficulty='Medium')
        self.assertEqual(workout.name, 'Test Workout')
