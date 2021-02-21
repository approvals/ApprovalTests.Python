s = '''
approvaltests.reporters.testing_reporter
approvaltests.string_writer
approvaltests.utils
approvaltests.reporters.generic_diff_reporter
approvaltests.reporters.diff_reporter
'''.strip().splitlines()[0:3]

import os
for module in s:
    command = 'monkeytype apply ' + module
    print(command)
    os.system(command)

