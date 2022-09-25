2. Next Week:
   1. do clean up:
   remove intro reporter, 
   clean up chain, 
   get all reporters is incomplete, 
   rename diffReporter to default diffReporter
   2. add help message
   3. create intro to reporters docs
      2. do a safeguarding for this
      3. clean up branch
3. Python Minimal 
   1. fix pypi key issues - Start here
   2. python parse requirements.prod.extras in minimal.py
   3. Figure out how to reference the two pypi projects in readme
   4. handle UNKNOWN VERSION situation in setup_utils.py better
4. In the start project should we have a test that confers that the extras are being loaded directly 
   1. What should that test be ? Pairwise, bs4
5. markdown snippets - regex (?<!(a>.*\n))```py
6. cached property for Namer.get_config 
7. setup github action to lint
   1. Do we make a github action whose sole purpose is to lint? 
   2. Options: Lint passes/fails or autocorrects? 
   3. Actions work well when simple. Make a lint.bat and go from there
8. linter - add flake8 to pycharm and tox
9. check all uses of default reporter in tests
10. Fail test if there are duplicate names - pylint ?
11. add checks to twine in github actions
12. make code more pythonic (method overloads vs default parameters)
13. _Have_ Oliver and Emily talk about pytest plugin is intergrated in hypoethesis
14. templated namer
    1. docs on implementing Approvaltests in CI
    2. file commiter reporter
    3. squence to animated gif writer
15. Property Tests
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

Co-Authored-By: Susan Fung <38925660+susanfung@users.noreply.github.com>

Co-authored-by: Nicholas A. Del Grosso <delgrosso.nick@gmail.com>
Co-Authored-By: jmasonlee <262853+jmasonlee@users.noreply.github.com>
Co-Authored-By: Bernhard Raml <1769280+SwamyDev@users.noreply.github.com>
