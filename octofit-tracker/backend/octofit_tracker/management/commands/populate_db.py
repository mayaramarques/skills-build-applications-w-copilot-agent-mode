from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Limpa as coleções
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Conecta ao MongoDB para criar índice único em email
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.users.create_index('email', unique=True)

        # Times
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Usuários
        users = [
            User(name='Tony Stark', email='tony@marvel.com', team='marvel'),
            User(name='Steve Rogers', email='steve@marvel.com', team='marvel'),
            User(name='Bruce Wayne', email='bruce@dc.com', team='dc'),
            User(name='Clark Kent', email='clark@dc.com', team='dc'),
        ]
        for user in users:
            user.save()

        # Atividades
        activities = [
            Activity(user='Tony Stark', type='run', duration=30, date='2023-01-01'),
            Activity(user='Steve Rogers', type='swim', duration=45, date='2023-01-02'),
            Activity(user='Bruce Wayne', type='cycle', duration=60, date='2023-01-03'),
            Activity(user='Clark Kent', type='fly', duration=120, date='2023-01-04'),
        ]
        for activity in activities:
            activity.save()

        # Leaderboard
        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=180)

        # Workouts
        workouts = [
            Workout(name='Pushup', description='Pushup exercise', difficulty='easy'),
            Workout(name='Pullup', description='Pullup exercise', difficulty='medium'),
            Workout(name='Squat', description='Squat exercise', difficulty='easy'),
            Workout(name='Deadlift', description='Deadlift exercise', difficulty='hard'),
        ]
        for workout in workouts:
            workout.save()

        self.stdout.write(self.style.SUCCESS('octofit_db populado com dados de teste!'))
