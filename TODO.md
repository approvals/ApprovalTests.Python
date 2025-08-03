2025-08-03
- [ ] F Improve scrubber help message when using unsupported format
- [ ] F DateScrubber.add_scrubber()
- [ ] d Document our local dialect of the commit notation in internal_documentation/commit_notation.md

2025-07-20
- [ ] Make it easier to switch between Windsurf and PyCharm
- [ ] Line numbers in build output and other custom scripts
- [ ] Solve startup with approvals (with Gregor)
- [ ] Scrubber ideas
   - [ ] replacement scrubber w/ case insensitive
   - [ ] log if not found

2025-07-06
- [ ] If using a custom comparator, maybe need a custom reporter
   - Write a document
   - A custom comparator already does the analysis, want to see that in the reporter
   - See Discord conversation: https://discord.com/channels/1349240939406819409/1349244369240195153/1391466948323442881
   - Example, comparing two pieces of code. Maybe we want to compare the AST not the original text.


2025-06-15
- [ ] dependabot linter
- [ ] explore uv and Mise
- stuff from last week

2025-06-01
- [ ] 🐜 Cascade running build_and_test reports success before running the tests - "run as blocking"
- [ ] Explore how to change the audible feedback from Cascade to make it less annoying - shorter and less loud
- [ ] reverse the dependency order of requirements.*.txt
- [ ] switch to uv / eliminate Tox 


2025-04-20
- [ ] in Python: rename run_tests -> build_and_test
    - [ ] rename `run_tests_and_format_code.sh` to what?
    - [ ] Jay wants to remove `.sh`
    - [ ] What is the impact on TAB-completion?
- [ ] mypy in Python
- [ ] fix disabled test for inline whitespace
- [ ] mypy in CommonScripts - tox?
- [ ] setup.approval_utilities.py and setup.py are different but should not be
- [ ] packaging has deprecation warnings
 
 
2025-03-23 
  - Discussion: what to do about unused imports
   
- [ ] Scripts to clean up approvals
     - [ ] Check if there's a Python `Once` facility
       - Wrap download_if_needed with Once
- [ ] clean up FileApproverTests
- [ ] Move the failed comparsion test to it's own file
- [ ] 2025-01-19 Make a long-term fix for the situation where a test has a destructive command
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
      Please note: we found this broken link [Capture .received. files from CI]
8.   * [ ]  this link: 
   * [Capture .received. files from CI](https://github.com/approvals/ApprovalTests.Java/blob/master/approvaltests/docs/explanations/how_to/CaptureFilesFromCI.md)
  


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


QUESTION
How to connect a Jetbrains product to a remote workspace.
1. PR to mobti.me to make ding the default
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
