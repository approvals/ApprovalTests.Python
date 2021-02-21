s = '''
tests.reporters.test_genericdiffreporter
tests.reporters.test_pycharm_reporter
tests.reporters.test_python_native_reporter
tests.reporters.test_reporter
tests.test_asserts
tests.test_combinations
tests.test_fileapprover
tests.test_list
tests.test_namer
tests.test_scenarios
tests.test_verify
approvaltests.reporters.generic_diff_reporter
approvaltests.reporters.diff_reporter
'''.strip().splitlines()[0:4]

import os
# pytest --monkeytype-output=./monkeytype.sqlite3
# monkeytype list-modules
for module in s:
    command = 'monkeytype apply ' + module
    print(command)
    os.system(command)

