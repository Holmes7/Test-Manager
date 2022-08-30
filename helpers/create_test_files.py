import os
from .utils import clean_directory
from test_manager import data_path


def prepare_problem_files(problem_id, sample_tests):
    problem_path = os.path.join(data_path, problem_id)
    if os.path.isdir(problem_path):
        clean_directory(problem_path)
    else:
        os.mkdir(problem_path)

    for test in sample_tests:
        add_sample_test(problem_id, test)


def add_sample_test(problem_id, sample_test):
    problem_path = os.path.join(data_path, problem_id)
    tests_dir_list = os.listdir(problem_path)
    max_int = 0
    for test in tests_dir_list:
        max_int = max(int(test), max_int)

    test_name = str(max_int + 1)
    test_path = os.path.join(problem_path, test_name)
    os.mkdir(test_path)
    create_test_files(test_path, sample_test)


def create_test_files(test_dir, test):
    input_file = os.path.join(test_dir, "input.txt")
    output_file = os.path.join(test_dir, "output.txt")
    expected_output_file = os.path.join(test_dir, "expected_output.txt")
    with open(input_file, "w") as fp:
        fp.write(test.test_input.strip(' \r\n'))
    with open(expected_output_file, "w") as fp:
        fp.write(test.expected_output.strip(' \r\n'))
    with open(output_file, "w") as fp:
        pass
