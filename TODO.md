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
- [x] move script from detect_and_remove_abandoned.bat -> python
- [x] Formatting locally (during the build?)
- 
2025-03-23 
-  [x] make a common repo for approvals ( so that it could be distributed with mypy) It exists, it does not work. 
  -   Potential Discussion: "Failed comparisons" vs. "Mismatched Files"
- 
- 
  - [x] change the checklist
  - Discussion: what to do about unused imports
- [ ] ensure approval test temp always has the .gitignore
    - [x] there are multiple places that call mkdir, but ONLY one that writes .gitignore
    
- [ ] Scripts to clean up approvals
     - [ ] Check if there's a Python `Once` facility
       - Wrap download_if_needed with Once
- [ ] clean up FileApproverTests
- [ ] Move the failed comparsion test to it's own file
- [ ] 2025-01-19 Make a long-term fix for the situation where a test has a destructive command
- [x] 2025-01-26 Easy "approve all" script
- [ ] docs: point to new architecture docs from python repo
- [ ] fix Namer and NamerBase

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
  


2. [x] update Cyber-dojo to have latest version of approvaltests.py and
   a. [x] verify which version of approval tests is in the new image that we just created
2. [ ] put an example of inline approvals into cyber-dojo
3. [ ] add JQ (nitsan created repo and submitted an issue)

-----  older stuff below ----
   1. [ ] extract SQL utils

7. [ ] copmarison after VCR (video recorder) hybrid of Executable Command 
   1. executatble ALONE
   2. VCR (python version of executable command )
   3. use both Executable command and VCR
8. to consider:
9. [ ] do we want to SPLIT up the Command Executer from the Command Generator 
Key x = done, - = started

notes: 
1. [ ] update Cyber-dojo to have latest version of approvaltests.py and


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
3. Logging decorator



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

1. Randomize order of tests in pytest plugin
