s = '''
approvaltests.reporters.multi_reporter
approvaltests.reporters.python_native_reporter
approvaltests.reporters.received_file_launcher_reporter
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

