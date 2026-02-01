
- [ ] OS FIrstWorkingReporter of everything frmo the same OS
- [ ] group diff reporter of everythingin the same group
- [ ] eliminate reporters.json
- [ ] IntelliJ is a side quest
- [ ] extract repoters.csv to its own repo
- [ ] clean up hand-coded rerpoters









- Help SeleniumLibrary update ApprovalTests. See https://github.com/robotframework/SeleniumLibrary/blame/c5c21ea2eb44d7e76619f96210d1f28c859f3aee/requirements-dev.txt#L6

- [ ] e uv cache doesn't respect `.python-version`
   - ideas/options:
      - clear the cache in `build_and_test`
      - use `uv pip --no-cache` DONE
         - problem: need to remember to rm the venv after changing python versions
         - idea: advertize the current actual python used version on every mise task execution 
      - guess: migrate to `pyproj.toml`, will solve this
         - how will we handle CI matrix?
      - write a `clean` script
          - git clean -xdf (to delete venv)
          - mise exec -- uv cache clean
          - mise uninstall --all
          - mise cache clear

      - define a custom cache key based on `.python-version`
      - in the python version checklist, clear cache
         - [ ] edit `.python-version`
         - [ ] run `uv cache clean`

- [ ] `set_python_version` script, which also removes the venv

- [ ] continuous AI loop experiment
   - [x] manual one-line linting experiment
   - [x] get python script to work: AI fixing script
   - [x] test for ai_fixer_loop argument parser
   - [ ] implement worker scripts for lint

- [ ] how to make a dev release (with Jay)
- [ ] Continuous Delivery (with Jay)
   - [ ] https://test.pypi.org/ credentials
   - [ ] test_current_release against https://test.pypi.org/
   - [ ] every commit releases to https://test.pypi.org/

2025-08-24
- [ ] more root dir cleanup
- [ ] remove mypy suppressions and fix

2025-08-17
- [ ] look at garbage collect of the with statement
- [ ] promote _clear_custom_scrubbers to public and give instructions in the feature file
- [ ] test this add_scrubber.md in java

2025-08-03
- [ ] d Document our local dialect of the commit notation in internal_documentation/commit_notation.md
        make this easy to refer to for NEW people. 
        Consider: pasting it into chat at start of day
        Consider: verbalize this during opening notice
        HMW (How Might We) help people who join late?? 
