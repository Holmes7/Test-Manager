import sublime
import os
import shutil
from test_manager import data_path


def set_problem(view, problem_id):
    for viewx in sublime.active_window().views():
        viewx.set_status("Problem", problem_id)


def get_problem(view):
    problem_code = view.get_status("Problem")
    if problem_code == "":
        raise Exception("Add or Select a problem first. The problem code will be visible in the status bar (bottom bar) once a problem is selected")
    return problem_code


def get_file_name(view):
    file_name = view.file_name()
    if file_name is None:
        raise Exception("Run the command with your program file in view")
    return file_name


def write_panel(text):
    win = sublime.active_window()
    panel = win.create_output_panel("test-manager-panel")
    panel.settings().set("gutter", False)
    panel.set_read_only(False)
    panel.run_command("append", {"characters": text})
    panel.set_read_only(True)
    win.run_command('show_panel', {"panel": "output.test-manager-panel"})


def clear_data_folder():
    clean_directory(data_path)


def clean_directory(path):
    shutil.rmtree(path)
    os.mkdir(path)
