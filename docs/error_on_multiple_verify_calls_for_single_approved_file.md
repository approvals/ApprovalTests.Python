# Background

Using the same approved file more than once can be useful, but it is rarely the case. See [](how_to/verify_both_logs_and_results.md)

# Current Behaviour

Approval Tests allows the same approved file to be used more than once.
The use case where two implementations are expected to have the same result.
In practice this is a rare scenario.
The issue is that most times this is confusing, when by accident the same approved file is reused. For example by having two `verify`s in a single test.

# Proposed Behaviour

Approval Tests will throw an error if the same approved file is used more than once.

There should be a way to still allow multiple `verify` per approved file for the rare 
- How it will work:


- you can turn it on by doing:
  - 
  - Proposed mechanism #1: Environment variable
    - It would be an option to use that ENV variable,  and 
      - If you are NOT using that ENV Variable then NOTHING Changes. 
      - local to whatever you are setting it on
      - 
  - Proposed mechanism #2: Use options
    - allow you to set global options that would take effect for your whole test suite
    - and the theory is: that would allow you to set this gloabally
    - CONCERN: we are not sure this will work the way we expect
