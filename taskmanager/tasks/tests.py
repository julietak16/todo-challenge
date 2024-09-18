from django.test import TestCase
from django.contrib.auth.models import User
from .models import Task

class TaskTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser")
        Task.objects.create(user=user, title="Task 1", completed=False)

    def test_task_creation(self):
        task = Task.objects.get(title="Task 1")
        self.assertEqual(task.title, "Task 1")

