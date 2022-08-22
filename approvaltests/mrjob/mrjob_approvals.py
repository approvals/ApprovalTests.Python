from io import BytesIO
from itertools import product

from mrjob.job import MRJob
from approvaltests import verify, verify_all_combinations


def verify_map_reduce(mr_job_under_test: MRJob, test_data: str) -> None:
    storyboard = print_map_reduce_job(mr_job_under_test, test_data)
    verify(storyboard)


def print_map_reduce_job(mr_job_under_test: MRJob, test_data: str) -> str:
    storyboard = f"{test_data}\n\nMap reduces to:\n\n"
    mr_job_under_test.sandbox(stdin=BytesIO(test_data.encode("utf-8")))
    with mr_job_under_test.make_runner() as runner:
        runner.run()
        results = mr_job_under_test.parse_output(runner.cat_output())
        for key, value in sorted(results):
            storyboard += f"{key}:{value}\n"
    return storyboard


def verify_templated_map_reduce(map_reduction, input_creator, params):
    inputs = product(*params)
    storyboard = ""
    for input in inputs:
        storyboard += f"===================\n\n{input} =>\n"
        data = input_creator(*input)
        storyboard += f"{print_map_reduce_job(map_reduction, data)}\n"
    verify(storyboard)
