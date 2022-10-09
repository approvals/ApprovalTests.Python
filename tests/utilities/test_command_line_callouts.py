from approvaltests import verify
import subprocess


def test_fizzbuzz_verify_range_1_to_100():
    # verify(command.run(
    #     ["bash", "-c", "jaq -n 'range(100) | .+1' | jaq -f fizzbuzz.jq"]).output.decode("utf8"))
    verify(subprocess.check_output('jq -n \"range(100) | .+1\" ', shell = True, universal_newlines = True))