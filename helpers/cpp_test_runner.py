import sublime
import subprocess
import os


class Cpp:
    def __init__(self, program_file):
        self.program_file = program_file
        self.executable_file = program_file[:len(program_file)-4]

    def run_all_tests(self, problem_path, timelimit):
        verdict, description = self.compile()
        if verdict is not None:
            return f'{verdict}\n{description}'
        s = sublime.load_settings("test_manager.sublime-settings")
        test_id = 1
        result = ""
        while True:
            test_path = os.path.join(problem_path, str(test_id))
            if not os.path.isdir(test_path):
                break
            input_file = os.path.join(test_path, "input.txt")
            output_file = os.path.join(test_path, "output.txt")
            expected_output_file = os.path.join(test_path, "expected_output.txt")
            verdict, description = self.run_test(input_file, output_file, expected_output_file, timelimit)
            result += f'Test {test_id}: {verdict}\n'
            if verdict in s.get("show_input"):
                with open(input_file, "r") as fp:
                    result += f"Input\n{fp.read()}"
            if verdict in s.get("show_output"):
                with open(output_file, "r") as fp:
                    result += f"\nOutput\n{fp.read()}"
            if verdict in s.get("show_expected_output"):
                with open(expected_output_file, "r") as fp:
                    result += f"\nExpected Output\n{fp.read()}"
            if verdict in s.get("show_error_description"):
                result += f"{description}"
            test_id += 1
        if os.path.isfile(self.executable_file):
            os.remove(self.executable_file)
        return result

    def run_test(self, input_file, output_file, expected_output_file, timelimit):
        cmd = self.executable_file
        try:
            fin = open(input_file, 'r')
            fout = open(output_file, 'w')
            proc = subprocess.run(
                cmd,
                stdin=fin,
                stdout=fout,
                stderr=subprocess.PIPE,
                timeout=timelimit,
                universal_newlines=True,
                shell=True
            )
            if proc.returncode != 0:
                print(proc.stderr)
                return "RE", proc.stderr
            else:
                return self.match_output(output_file, expected_output_file)
        except subprocess.TimeoutExpired:
            return "TLE", ""

    def match_output(self, output_file, expected_output_file):
        with open(output_file) as fp:
            o_str = fp.read()
            o_str = o_str.strip(" \r\n")

        with open(expected_output_file) as fp:
            eo_str = fp.read()

        if o_str == eo_str:
            return "AC", ""
        else:
            return "WA", ""

    def compile(self):
        s = sublime.load_settings("test_manager.sublime-settings")
        cmd = "{0} -Wall -Wextra -O2 -fwrapv -Wfloat-equal -Wconversion -std={1} -o {2} {3}".format(
            s.get("cpp_executable"),
            s.get("cpp_std"),
            self.executable_file,
            self.program_file
            )
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            shell=True
        )
        if proc.returncode != 0:
            return "CE", proc.stderr
        else:
            return None, None