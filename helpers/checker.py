from .utils import get_problem
from test_manager import data_path
from .cpp_test_runner import Cpp
import traceback
import os


def check_program(view):
    try:
        problem_code = get_problem(view)
        program_file = view.file_name()
        problem_path = os.path.join(data_path, problem_code)
        if program_file.endswith(".cpp"):
            test_runner = Cpp(program_file)
        else:
            raise Exception("{} file type not compatible".format(program_file))

        return test_runner.run_all_tests(problem_path, timelimit=1)
    except Exception as err:
        print(traceback.format_exc())
        return str(err)
