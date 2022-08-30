import sublime
import sublime_plugin
import re
from .helpers.utils import write_panel, set_problem
from .helpers.create_test_files import prepare_problem_files
from .helpers.judge import get_problem_object
import traceback


class AddProblemCommand(sublime_plugin.TextCommand):
    def run(self, edit, problem_url):
        try:
            self.problem_obj = get_problem_object(problem_url)
            problem_id = self.problem_obj.get_problem_id()
            set_problem(self.view, problem_id)
            sample_tests = self.problem_obj.parse_samples()
            prepare_problem_files(problem_id, sample_tests)
        except Exception as error:
            write_panel(str(error))
            print(traceback.format_exc())

    def input(self, args):
        return ProblemUrlInputHandler()


class ProblemUrlInputHandler(sublime_plugin.TextInputHandler):
    def name(self):
        return "problem_url"

    def placeholder(self):
        return "Enter problem url"
