1. python type hints - use mypy linter to check it - see code snippet below
1. setup github action to lint
1.  linter - add flake8 to pycharm and tox
1. check all uses of default reporter in tests
1. change setup.py to pull in requirements.txt - and check requirements
1. Fail test if there are duplicate names - pylint ?
1.  add checks to twine in github actions
1. markdown snippets
1. starter projects
1. powershell scripts
1. new feature: options support
1. make code more pythonic (method overloads vs default parameters)
1.  Agree on defaults: should be \n instead of os specific when writing, BOM on new file creation,
1.   the new file creation handles writing with correct encoding
1.  combination approvals needs line ending option
1.  error output is too confusing
1.  add tests to test the installed library - integration or system tests. For example, to confirm that JSON reporter files work. tox might help us.

```python

  def test_mypy(self) -> None:
       try:
           import mypy.api
       except ImportError:
           print("mypy not found")
           self.skipTest("mypy not found")
       stdout, stderr, exit_code = mypy.api.run([
           '--config-file', 'mypy.ini',
           SCRIPT_DIR,
       ])
       self.assertEqual(0, exit_code, "\n\n" + stdout + stderr)
```

1. Look at issues https://github.com/approvals/ApprovalTests.Python/issues
1. Randomize order of tests in pytest plugin


Authors:
@claremacrae
@objarni
@tdpreece
@emilybache
@rzijp
@obestwalter
