import sublime
import sublime_plugin
from .helpers.utils import clear_data_folder


class ClearData(sublime_plugin.TextCommand):
    def run(self, edit):
        clear_data_folder()
