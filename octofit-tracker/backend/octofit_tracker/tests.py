from django.test import TestCase
from rest_framework.test import APIClient
from .models import Team, User, Activity, Workout, Leaderboard

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name="Marvel", description="Marvel team")
        self.user = User.objects.create(name="Spiderman", email="spiderman@marvel.com", team=self.team)
        self.workout = Workout.objects.create(name="Cardio", description="Run fast")
        self.workout.suggested_for.add(self.team)
        self.activity = Activity.objects.create(user=self.user, type="run", duration=30, date="2025-11-17")
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_api_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("users", response.data)

    def test_users_endpoint(self):
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_teams_endpoint(self):
        response = self.client.get("/api/teams/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_activities_endpoint(self):
        response = self.client.get("/api/activities/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_workouts_endpoint(self):
        response = self.client.get("/api/workouts/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_leaderboard_endpoint(self):
        response = self.client.get("/api/leaderboard/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
