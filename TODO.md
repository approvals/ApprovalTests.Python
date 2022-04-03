1. markdown snippets - regex (?<!(a>.*\n))```py
2. cached property for Namer.get_config 
3. setup github action to lint
   1. Do we make a github action whose sole purpose is to lint? 
   2. Options: Lint passes/fails or autocorrects? 
   3. Actions work well when simple. Make a lint.bat and go from there
4. linter - add flake8 to pycharm and tox
5. check all uses of default reporter in tests
6. Fail test if there are duplicate names - pylint ?
7. add checks to twine in github actions
8. make code more pythonic (method overloads vs default parameters)
9. _Have_ Oliver and Emily talk about pytest plugin is intergrated in hypoethesis
10. templated namer
    1. docs on implementing Approvaltests in CI
    2. file commiter reporter
    3. squence to animated gif writer
11. Property Tests
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
