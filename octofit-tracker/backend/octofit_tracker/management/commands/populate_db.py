from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient()
        db = client['octofit_db']

        # Test data for users
        users = [
            {"email": "user1@example.com", "name": "User One"},
            {"email": "user2@example.com", "name": "User Two"},
        ]
        db.users.insert_many(users)

        # Test data for teams
        teams = [
            {"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]},
            {"name": "Team Beta", "members": []},
        ]
        db.teams.insert_many(teams)

        # Test data for activities
        activities = [
            {"user": "user1@example.com", "type": "running", "duration": 30},
            {"user": "user2@example.com", "type": "cycling", "duration": 45},
        ]
        db.activity.insert_many(activities)

        # Test data for leaderboard
        leaderboard = [
            {"user": "user1@example.com", "points": 100},
            {"user": "user2@example.com", "points": 80},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Test data for workouts
        workouts = [
            {"name": "Workout A", "description": "Full body workout"},
            {"name": "Workout B", "description": "Cardio workout"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
