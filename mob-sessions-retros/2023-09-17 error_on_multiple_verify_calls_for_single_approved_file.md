# Background

Using the same approved file more than once can be useful, but it is rarely the case. See [verify_both_logs_and_results.md](/docs/how_to/verify_both_logs_and_results.md)

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
    - 
  - We did:  Option 3
  - we added a configuration fuction to set a Global Boolean 

9/17/2023 Possible TODOs:
we have an intentionally failing test:
we want to see the failure
the code needs refactoring:
there if statements could be encapsulatedin into a nethod, or even into its own calss
we said: allow people to still have multiple vaerifys if they want to use it. 
  so we would need to implement 
- move back to approvals (cutently in Fileapprovals)
CONSIDER
building a testing framework
  - we need to get used to the fact that a test could fail.
    - we designed it to fail. and that failure is the expected result.
    - SUGGESTION:  make it part of the capbility:  
      - a test is expected to fail and in that situation the failure is expected and wanted 
- How could we implmenet that?
  - could we add a Complication layer?
  - could we use a Puython test feature that expects the result to be a failure?


This test should fail

```python
def test_multiple_calls_to_verify():
  error_on_multiple_verify_calls(True)
  verify("call to verify")
  verify("call to verify")
```

# Retro

## How did that feel?

- at one point felt confused: moving to using the 'previous_approved' variable
  - but, as we went through it, it made more sense
  - when we only had a single variable - FEAR - "I think we're going to break stuff"; but later felt safer
- Happy when D was talking through her intentions, you learn something during those 4 minutes
- Happy to be practicing asking more Qs today

- Pattern we used today:  Create a feature toggle, add new functionality then test it by adding the functionality inside the toggle 
create an isolated safe space to make changes to the code
that is Protected by a toggle
leave it OFF by default.
and then you can do whatever you want inside that Feature Toggle (a configuration toggle)
that allows us to push incomplete work.
Because the users are VERY unlikely to find the toggle
this would allow us to release (if we had to or wanted to release it )

- Strong pairing / mobbing - fun having someone else typing, makes things easier by giving a higher level intention

## Learned

- Refactor -> Move
- python globals, class variables

## Liked
- we are building a testing framework
  - we need to get used to the fact that a test could fail.
    - we designed it to fail. and that failure is the expected result.
    - SUGGESTION:  make it part of the capbility:  
      - a test is expected to fail and in that situation the failure is expected and wanted 
      - 
- we have a safe space
  - allows pretending that "it's going to be ok"
  - Even without any help, felt like was going somewhere
  - Willing to flounder, as a coach let people flounder, it's ok
  - Potentially can say "I'm here for you, I'll help however you like", or "I may ask Qs if that will help"
  - N  it is interesting to see WHAT at Big differnce Your psychological space makes 
    - for someone being willing to try something. 
  - there is a pradox:  we are dealing with such a concrete profession.
    - yet in order to make progress and learn and understand you need to TAKE CARE of the Soft stuff. 
      - yet the psychological safety 
- it helps to ask for what you like
  - e.g. changing the rotation order
- Benefit of keeping two people who are both familiar with the domain
- next to eacj other in the rotation:
- you get to see:  two expienced people working together

- today's pattern we tried both,  we had interleave
- D asked to keep comments around longer than N prefers
- D asked and the mob kept the extra lines which helped D

- habit:  we started with a document.  rather than starting with the Code. 
- it helped clarify exactly what we wanted to do.
- that helped S understand what we were doing. 
- N      said I feel good about doing this 

- noticed: the emphasis on TDD
- Let's see a failing test, what would that failing test look like. 

- a problem with mobbing is
  - you need to be able/willing to be vulerable
  - your willingness is dependent on the psych safety of the environment as well as your own psych space
