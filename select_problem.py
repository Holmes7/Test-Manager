import sublime
import sublime_plugin
from test_manager import data_path
from .helpers.utils import set_problem
import os


class SelectProblemCommand(sublime_plugin.TextCommand):
    def run(self, edit, problem_code):
        set_problem(self.view, problem_code)

    def input(self, args):
        return ListProblemInputHandler()


class ListProblemInputHandler(sublime_plugin.ListInputHandler):
    def name(self):
        return "problem_code"

    def list_items(self):
        return os.listdir(data_path)
