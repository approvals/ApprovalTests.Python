1. markdown snippets
3. cached property for Namer.get_config 
4. setup github action to lint
5. linter - add flake8 to pycharm and tox
6. check all uses of default reporter in tests
7. change setup.py to pull in requirements.txt - and check requirements
8. Fail test if there are duplicate names - pylint ?
9. add checks to twine in github actions
10. new feature: options support
11. make code more pythonic (method overloads vs default parameters)
12. Agree on defaults: should be \n instead of os specific when writing, BOM on new file creation,
13. the new file creation handles writing with correct encoding
14. combination approvals needs line ending option
15. error output is too confusing (from Clare: logged as https://github.com/approvals/ApprovalTests.Python/issues/97)
16. add tests to test the installed library - integration or system tests. For example, to confirm that JSON reporter files work. tox might help us.
17. Have Oliver and Emily talk about pytest plugin is intergrated in hypoethesis
18. Future things
19. Pairwise
20. templated namer
    1. docs on implementing Approvaltests in CI
    2. file commiter reporter
    3. squence to animated gif writer
21. Get starter project to pass CI with version
22. Property Tests
23. eval(any.__repr__) == any
24. create(any_reporter) == create(any_reporter)
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
```.ini
[mypy]
python_version = 3.7
pretty = True
no_incremental = True
ignore_missing_imports = True

strict = True
    ;;;;;;;;  `strict` enables the following flags:
    ; --check-untyped-defs
    ; --disallow-any-generics
    ; --disallow-incomplete-defs
    ; --disallow-subclassing-any
    ; --disallow-untyped-calls
    ; --disallow-untyped-decorators
    ; --disallow-untyped-defs
    ; --no-implicit-optional
    ; --no-implicit-reexport
    ; --strict-equality
    ; --warn-redundant-casts
    ; --warn-return-any
    ; --warn-unused-configs
    ; --warn-unused-ignores
no_site_packages = True
disallow_any_unimported = True
disallow_any_expr = True
disallow_any_decorated = True
disallow_any_explicit = True
strict_optional = True
warn_no_return = True
warn_unreachable = True
```
Authors:
@claremacrae
@objarni
@tdpreece
@emilybache
@rzijp
@obestwalter
