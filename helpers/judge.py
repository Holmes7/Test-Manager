import re
from .atcoder import AtcoderProblem
from .codeforces import CodeforcesProblem


def get_problem_object(problem_url):
    if re.search("atcoder", problem_url):
        return AtcoderProblem(problem_url)
    elif re.search("codeforces", problem_url):
        return CodeforcesProblem(problem_url)
    else:
        raise Exception("Invalid url: {}".format(problem_url))
