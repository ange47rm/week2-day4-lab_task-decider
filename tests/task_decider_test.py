import unittest
from src.task_decider import get_preffered_option
from src.task import Task


class TestTaskDecider(unittest.TestCase):
    def setUp(self):
        self.wash_dishes  = Task('Wash the dishes', 5)
        self.cook_dinner = Task('Cook the dinner', 10)
        self.clean_windows = Task('Clean the windows', 50)

    def test_wash_dishes__is_preferred__over_cook_dinner(self):
        self.assertEqual('Wash the dishes', get_preffered_option(self.wash_dishes, self.cook_dinner))

    def test_wash_dishes__is_preferred__over_cook_dinner_order_swap(self):
        self.assertEqual('Wash the dishes', get_preffered_option(self.cook_dinner, self.wash_dishes))

    
    def test_cook_dinner__is_preferred__over_clean_windows_order_swap(self):
        self.assertEqual('Cook the dinner', get_preffered_option(self.clean_windows, self.cook_dinner))

    def test_cook_dinner__is_preferred__over_clean_windows(self):
        self.assertEqual('Cook the dinner', get_preffered_option(self.cook_dinner, self.clean_windows))
    

    def test_clean_windows__is_preferred__over_wash_dishes(self):
        self.assertEqual('Clean the windows', get_preffered_option(self.clean_windows, self.wash_dishes))    
    def test_clean_windows__is_preferred__over_wash_dishes_order_swap(self):
        self.assertEqual('Clean the windows', get_preffered_option(self.wash_dishes, self.clean_windows))