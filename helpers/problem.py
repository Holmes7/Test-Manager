from abc import ABCMeta, abstractmethod


class SampleTest:
    def __init__(self, test_input, expected_output):
        self.test_input = test_input
        self.expected_output = expected_output

    def __repr__(self):
        return 'Input: {0}\nOutput: {1}'.format(self.test_input, self.expected_output)


class Problem(metaclass=ABCMeta):
    def __init__(self, problem_url):
        self.problem_url = problem_url

    @abstractmethod
    def parse_samples(self):
        pass

    @abstractmethod
    def get_problem_id(self):
        pass

    def create_test_files():
        pass
