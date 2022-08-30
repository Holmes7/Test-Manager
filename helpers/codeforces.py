from .problem import Problem
from test_manager.requests import get
from test_manager.bs4 import BeautifulSoup
from .problem import SampleTest
import re


class CodeforcesProblem(Problem):
    contest_regex = r"/contest/\d+/problem/\w"
    gym_regex = r"\d+/problem/\w"
    problemset_regex = r"\d+/\w"

    def get_problem_id(self):
        problem_id = re.search(self.contest_regex, self.problem_url)
        if problem_id:
            return problem_id.group().replace("/problem/", "").replace("/contest/", "")
        problem_id = re.search(self.gym_regex, self.problem_url)
        if problem_id:
            return problem_id.group().replace("/problem/", "").replace("/gym/", "")
        problem_id = re.search(self.problemset_regex, self.problem_url)
        if problem_id:
            return problem_id.group().replace("/", "")
        raise Exception("Invalid url: {}".format(self.problem_url))

    def parse_samples(self):
        page = get(self.problem_url).text
        input_divs = BeautifulSoup(page, "html.parser").find_all('div', {"class": "input"})
        input_tests = []
        for inp in input_divs:
            pre = inp.find('pre')
            test = ""
            for div in pre.find_all('div'):
                test += div.text
                test += "\n"
            input_tests.append(test)
        output_divs = BeautifulSoup(page, "html.parser").find_all('div', {"class": "output"})
        output_tests = []
        for out in output_divs:
            output_tests.append(out.find('pre').text)
        total = len(input_tests)
        sample_tests = []
        for i in range(total):
            test_obj = SampleTest(test_input=input_tests[i], expected_output=output_tests[i])
            sample_tests.append(test_obj)
        return sample_tests
