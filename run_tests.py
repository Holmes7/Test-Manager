import sublime
import sublime_plugin
from .helpers.checker import check_program
from .helpers.utils import write_panel


class RunTests(sublime_plugin.TextCommand):
    def run(self, edit):
        result = check_program(self.view)
        write_panel(result)
