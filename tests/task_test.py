import unittest
from src.task import Task


class TestTask(unittest.TestCase):
    def setUp(self):
        self.wash_dishes  = Task('Wash the dishes', 5)
        self.cook_dinner = Task('Cook the dinner', 10)
        self.clean_windows = Task('Clean the windows', 50)

    def test_task_has_description(self):
        self.assertEqual('Wash the dishes', self.wash_dishes.description)

    def test_task_has_duration(self):
        self.assertEqual(10, self.cook_dinner.duration)

 