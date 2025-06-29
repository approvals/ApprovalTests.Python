2025-06-15
- [x] format pushes to main (maybe?)
     potential bug in repo automation?? bug:  if you createa branch in app test pthon, sometimes it will get merged to main. :O
     make a change that requires a format and see if it gets merged to main
   - [ ] consider creating an org-level workflow template
- [ ] Datescrubber PRs
- [ ] dependabot linter
- [ ] explore uv and Mise
- stuff from last week

2025-06-01
- [ ] 🐜 Cascade running build_and_test reports success before running the tests - "run as blocking"
- [ ] Explore how to change the audible feedback from Cascade to make it less annoying - shorter and less loud
- [x] Publish soon (it has been a while - 7 April)
   - [x] make a list of the changes since the last time we published (to help us decide if we should release)
   - [x] add to the approved list: git log, status, fetch, diff
- [ ] consider creating a run book for the release process
- [ ] reverse the dependency order of requirements.*.txt
- [ ] switch to uv / eliminate Tox 


2025-04-20
- [x] how we run integration tests
    - rename tox entry point and the test
- [ ] in Python: rename run_tests -> build_and_test
    - [ ] rename `run_tests_and_format_code.sh` to what?
    - [ ] Jay wants to remove `.sh`
    - [ ] What is the impact on TAB-completion?
- [ ] mypy in Python
- [ ] fix disabled test for inline whitespace
- [ ] mypy in CommonScripts - tox?
- [ ] setup.approval_utilities.py and setup.py are different but should not be
- [ ] packaging has deprecation warnings
 
2025-04-06
In `CommonScripts` repo:
- [ ] move script from detect_and_remove_abandoned.bat -> python
-  [ ] finish exploratory test 
    - [ ] Does it actually delete things?
    - [ ] Showed the wrong files (`str`/`Path` comparison?)
- [ ] Formatting locally (during the build?)
- 
- 2025-03-23 
-  [x] make a common repo for approvals ( so that it could be distributed with mypy) It exists, it does not work. 
  -   Potential Discussion: "Failed comparisons" vs. "Mismatched Files"
- 
- 
  - [x] change the checklist
  - install update to CoPilot
  - PR to mobtime app to show the next person (see Susan and Diana's work)
  - Discussion: what to do about unused imports
- [ ] ensure approval test temp always has the .gitignore
    - there are multiple places that call mkdir, but ONLY one that writes .gitignore
  Possible work for today 2025-3-23
    - [] 1 does the last feature actually work?  (detecting abandond approve files)
    - [] 2 make a common repo for approvals ( so that it could be distributed with mypy) It exists, it does not work. 
    - [] 3 experiemnt with AI copilot in the editor with the new Agent mode 
      -         install update to CoPilot
    - [] 4 add to checklist: review open issues and PRs (at least 1x month )
    - [] 5 PR to mobtime app to show the next person (see Susan and Diana's work)
    - 
    
- [ ] Scripts to clean up approvals
     - [ ] Fix detect_and_remove_abandoned.bat
     - [ ] Check if there's a Python `Once` facility
       - Wrap download_if_needed with Once
     - [ ] test the `approve_all` script
     - [ ]  Consider whether this creates an acceptable run-time dependency
- [ ] clean up FileApproverTests
- [ ] Move the failed comparsion test to it's own file
- [ ] 2025-01-19 Make a long-term fix for the situation where a test has a destructive command
- [ ] 2025-01-26 Easy "approve all" script
  - Llewellyn says "1. Create the .failed_comparison.log"
  - Make a failed_comparison log and an approve_all script, in Python. Model it after ApprovalTests.Java. 
  - Requirements:
    - [X] Create the .failed_comparison.log
      - [X] Every time you run the tests, it creates a fresh .failed_comparison.log
      - [X] failed_comparison.log contains a list of all of the tests that failed, with a "goes-to" arrow for the approval file that it would be saved in, e.g.:
      -    `C:\path\to\test.received.txt -> C:\path\to\test.approved.txt`
    - [ ] Download the utility scripts
      - [ ] approved_all.sh approves all the files that are listed in the failed_comparison.log
      - Tip: start with the files at https://github.com/approvals/ApprovalTests.Java/tree/master/resources
- [ ] 2024-09-22 discuss access to repo beyond just Llewellyn's user
- [ ] clean-up old PRs (there are 3 from Dec 2023)
- [ ] docs: point to new architecture docs from python repo
- [ ] mypy in the build
- [ ] fix Namer and NamerBase
- [ ] ReporterThatCreatesAnApprovalScript
  - [ ] Write unit tests for this (automated)  see the manual tests in this file: test_reporter_that_creates_an_approval_script.py
  - [ ] Create log and approve_all_failing.sh

- FUTURE TODO
Fix this timer - [see draft of proposed issue](https://docs.google.com/document/d/1avKRVobADSIxXiwRQt0o3Ohawvdbbo4UDlWtyRYhuRo/edit?usp=sharing)
1) show all three roles
Typer: talker and Next
2) label the roles to match what we like
New Timer will show: 
Typer: <typer name>
And in lower right:
Talker: <talker name>
Next: <name of next person>


> How do we know that everything works in both Pytest and Unittests?
> 
[ ] Test fail if mariadb is in the requirements for linux

POssible FEATURE  
Create an API to add a REPORTER.[test_inline_approvals.py](tests%2Ftest_inline_approvals.p[ok.approved.txt](ok.approved.txt)y)
    now we have a combined reporter  and then ?? only the last one works? 

Inline Approvals Bugs
0. [ ] InlineOptions to show diffs
1. [ ] rename all of the reporters to start with the word report
2. [ ] check all reporters return True or False
    4. [ ] add mypy to the CI (type hints exist and they are being inforced)
   4. 2024-04-21 - The issue is in MRJob. Need probably need to move to spark. this should probably be done with Jacqueline present
3. [ ] make it so that approvals works with Python 12
4. [ ] Improve verify_all for no header
        Expects VerifyAll to have a header
        this is mandatory For PYthon Approval Tests
        added an example to Test_inline_approvals.py
        see: def test_uppercase_with_verify_all():
5. [ ] expand functionality of parse_doc_string     NOTE: this is WIP from 3/3/24 parse inputs
   2. [ ] =>, :
      3. [ ] maybe not only docstring but any text or approved file?
   4. [ ] multiple parameters 1, 2, 3 -> 
   5. [ ] converter parse(to_integer)
   6. [ ] some relationship between the output formatter and the parser
      7. [X ] Move explainations to ApprovalTests.Documentation 
      Please note: we found this broken link [Capture .received. files from CI]
8.   * [ ]  this link: 
   * [Capture .received. files from CI](https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/explanations/how_to/CaptureFilesFromCI.md)
  


1. disable the CMD key in this Any Desk  (Nitsan suggested)
2. [x] update Cyber-dojo to have latest version of approvaltests.py and
   a. [x] verify which version of approval tests is in the new image that we just created
2. [ ] put an example of inline approvals into cyber-dojo
3. [ ] add JQ (nitsan created repo and submitted an issue)

-----  older stuff below ----
2. [ ] run the test
2. [ ] Review what we have done
3. [ ] Clean up so things are ready for production
   1. [ ] extract SQL utils
4. [ ] write some docs
5. [ ] use it (as the users will )   Manual regression test
6. [ ] ship the code
   1. [ ] explore additional test that will Re-test the way other will use it
7. [ ] copmarison after VCR (video recorder) hybrid of Executable Command 
   1. executatble ALONE
   2. VCR (python version of executable command )
   3. use both Executable command and VCR
8. to consider:
9. [ ] do we want to SPLIT up the Command Executer from the Command Generator 
Key x = done, - = started

notes: 
1. [ ] update Cyber-dojo to have latest version of approvaltests.py and

What have we learned?
- How does approvals work in cyber-dojo?
- There are two docker images with python approvals: 1. pytest 2. unittest
- is the version number important?
- Does it use the pytest plugin at all? Or just pytest?
- set up Gitpod
- 


Possible problem:
we have linked the Execute command and the _____
when you run it
 there is the part about how to execute
 and there is ANOTHER part
that shows you the specific command that you ar trying to verify
it is not obvious how they are used
REALIZATION: 
Executatlbe command class is an Executable COmmand class    and
_____ (put it in the chat Lev)

QUESTION
How to connect a Jetbrains product to a remote workspace.
5. Mr job - need to be able to test against more than one line in a file.
1. PR to mobti.me to make ding the default
   4. Can we change the paradigm for how we do combinations with data and MRJob?
1. cyber-dojo bug - received file not being deleted 3
3. Continuing work on approvals-cli: 5
   4. Documentation
   5. Adding a binary
   6. Smarter namer
   7. test improvements - do we have all the tests we need?
4. Create a self-sufficient mob. 
   5. Need a reproducible anydesk machine
      6. Create other EC2 instances
      7. gitpod
      8. Llewellyn starts an instance and then someone joins with RDP
         9. Less comfortable -Github action that spins up an EC2 instance to launch the existing machine-
   6. Need a zoom that anyone can connect to
3. Logging decorator



5. 
6. Next Week:
   1. do clean up:
   clean up chain, 
   get all reporters is incomplete, 
   rename diffReporter to default diffReporter
   2. add help message
   3. create intro to reporters docs
      2. do a safeguarding for this
      3. clean up branch
7. Python Minimal 
   2. python parse requirements.prod.extras in minimal.py
   4. handle UNKNOWN VERSION situation in setup_utils.py better
8. In the start project should we have a test that confers that the extras are being loaded directly 
   1. What should that test be ? Pairwise, bs4
9. markdown snippets - regex (?<!(a>.*\n))```py
10. cached property for Namer.get_config 
11. setup github action to lint
    1. Do we make a github action whose sole purpose is to lint? 
    2. Options: Lint passes/fails or autocorrects? 
    3. Actions work well when simple. Make a lint.bat and go from there
12. linter - add flake8 to pycharm and tox
13. check all uses of default reporter in tests
14. Fail test if there are duplicate names - pylint ?
15. add checks to twine in github actions
16. make code more pythonic (method overloads vs default parameters)
17. _Have_ Oliver and Emily talk about pytest plugin is intergrated in hypoethesis
18. templated namer
    1. docs on implementing Approvaltests in CI
    2. file commiter reporter
    3. squence to animated gif writer
19. Property Tests
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
python_version = 3.8
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
Co-authored-by: Mohammed Anjum <mohammedanjum.dev@gmail.com>
Co-Authored-By: jmasonlee <262853+jmasonlee@users.noreply.github.com>
Co-Authored-By: Jay Bazuzi <jay@bazuzi.com>
Co-authored-by: Nicholas A. Del Grosso <delgrosso.nick@gmail.com>
Co-Authored-By: Bernhard Raml <1769280+SwamyDev@users.noreply.github.com>


imports aren't working correctly
