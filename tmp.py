s = '''
approvaltests.approval_exception
approvaltests.approvals
approvaltests.asserts
approvaltests.combination_approvals
approvaltests.command
approvaltests.core.namer
approvaltests.core.scenario_namer
approvaltests.file_approver
approvaltests.list_utils
approvaltests.pytest.namer
approvaltests.reporters.clipboard_reporter
approvaltests.reporters.diff_reporter
approvaltests.reporters.first_working_reporter
approvaltests.reporters.generic_diff_reporter
approvaltests.reporters.generic_diff_reporter_factory
approvaltests.reporters.multi_reporter
approvaltests.reporters.python_native_reporter
approvaltests.reporters.received_file_launcher_reporter
approvaltests.reporters.testing_reporter
approvaltests.string_writer
approvaltests.utils
'''.strip().splitlines()[0:10]

import os
for module in s:
    command = 'monkeytype apply ' + module
    print(command)
    os.system(command)

