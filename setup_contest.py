import sublime
import sublime_plugin
import re


class SetupContestCommand(sublime_plugin.TextCommand):
    def run(self, edit, contest_url):
        samples = parse_atcoder_samples(contest_url)

    def input(self, args):
        return ContestUrlInputHandler()


class ContestUrlInputHandler(sublime_plugin.TextInputHandler):
    def name(self):
        return "contest_url"

    def placeholder(self):
        return "Enter contest url"


class Contest:
    def __init__(self, contest_url):
        self.contest_url = contest_url
