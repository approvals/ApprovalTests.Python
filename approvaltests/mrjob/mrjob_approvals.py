from io import BytesIO
from mrjob.job import MRJob
from approvaltests import verify


def verify_map_reduce(mr_job_under_test: MRJob, test_data: str) -> None:
    storyboard = f"{test_data}\n\nMap reduces to:\n\n"
    mr_job_under_test.sandbox(stdin=BytesIO(test_data.encode("utf-8")))
    with mr_job_under_test.make_runner() as runner:
        runner.run()
        for key, value in mr_job_under_test.parse_output(runner.cat_output()):
            storyboard += f"{key}:{value}\n"
    verify(storyboard)
