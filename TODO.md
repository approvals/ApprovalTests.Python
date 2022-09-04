2. Next Week:
   1. fix python native reporter isn't in by default
   2. do a safeguarding for this
   3. clean up branch
3. Python Minimal 
   1. fix pypi key issues - Start here
   2. python parse requirements.prod.extras in minimal.py
   3. Figure out how to reference the two pypi projects in readme
   4. handle UNKNOWN VERSION situation in setup_utils.py better
5. In the start project should we have a test that confers that the extras are being loaded directly 
   1. What should that test be ? Pairwise, bs4
6. markdown snippets - regex (?<!(a>.*\n))```py
7. cached property for Namer.get_config 
8. setup github action to lint
   1. Do we make a github action whose sole purpose is to lint? 
   2. Options: Lint passes/fails or autocorrects? 
   3. Actions work well when simple. Make a lint.bat and go from there
9. linter - add flake8 to pycharm and tox
10. check all uses of default reporter in tests
11. Fail test if there are duplicate names - pylint ?
12. add checks to twine in github actions
13. make code more pythonic (method overloads vs default parameters)
14. _Have_ Oliver and Emily talk about pytest plugin is intergrated in hypoethesis
15. templated namer
    1. docs on implementing Approvaltests in CI
    2. file commiter reporter
    3. squence to animated gif writer
16. Property Tests
    1. eval(any.__repr__) == any
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
