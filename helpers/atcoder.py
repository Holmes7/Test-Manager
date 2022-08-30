from .problem import Problem
from test_manager.requests import get
from test_manager.bs4 import BeautifulSoup
from .problem import SampleTest
import re


class AtcoderProblem(Problem):
    problem_id_regex = r'a\wc\d\d\d_\w'

    def get_problem_id(self):
        problem_id = re.search(self.problem_id_regex, self.problem_url)
        if problem_id:
            return problem_id.group()
        else:
            raise Exception("Invalid url: {}".format(self.problem_url))

    def parse_samples(self):
        page = get(self.problem_url).text
        pre_list = BeautifulSoup(page, "html.parser").find_all('pre')
        total = len(pre_list)//2
        i = 1
        sample_tests = []
        for i in range(1, total, 2):
            test_obj = SampleTest(test_input=pre_list[i].text, expected_output=pre_list[i+1].text)
            sample_tests.append(test_obj)
        return sample_tests
