# Todos

-   [ ] example use case for vcr-like functionality, for instance **prompt an llm to rename variable**
    -   expected behavior is:
        -   input: prompt (`"suggest a better name for var X in the following code"`)
            -   please rename the name foo to smthg better

                ---

                ```
                function foo(a,b) {
                return a +b
                }
                ```
        -   output:
-   [ ] build it
    -   [ ]


Events:
    Nitsan:
        - Said hello
        - Decided to find a work item
        - wanted to release for the person who asked for it in our github issues and couldn't because we are not Llewellyn
        - Dropped that
        - Nitsan suggested ideas from his own private todo list
        - Picked the VCR thing
        - Made a TODO
        - Quickly went to writing a pseudo-code test for the purpose of documenting the intention
        - The pseudo-code became code. 
        - It wasn't perfect, but the pseudo-code became code
        - Approvaltests got us so far without any modifications
    Susan:
        - Made a barebones todo list
        - Went into the specifics on the first item in the todo list
        - Wrote the test cases we wanted to test:
          - That we sent the correct command and that we receive the expected output
        - Skipped the second failing test so we can focus on the first test
        - Built the first test
        - Made the CallLLM class
        - put in the command
        - added the code to call the OpenAI API
        - Modified the prompt so that the response was in a format we like

    Joss:
        - Started by making our goals for the session
        - decided on trying to make a vcr test or something that would mimic the functionality of a vcr test
        - Goal was to take the output of an LLM and parse it so that we could test only the useful bits of what it was giving us
        - did coding
        - Swapped 5 minutes to 3 minutes
        - Good that we took the time to make sure we understood what we were doing and how to do it
        - Did that instead of doing work on other people's turns
        - 
    Jacqueline:
        - 10m waiting for everybody, saw Nitsan's new cam
        - picked VCR tests with executable commands (wasn't sure how we might build this - so thought of a use case - prompting chatGPT for suggesting renames in code)
        - started a TODO list
        - Felt that not everybody understands - asked Nitsan to help with explaining
        - Nitsan started walking though pseudo-code, that later became code; I would have picked drawing
        - There were interesting points: leaning on the ensemble to move forward, even when not knowing exactly what to do - e.g. "prompt here"
        - Felling like things were slow - asked for faster rotations - 5m -> 3m
        - We got through impl an ExecutableCommand - piecing pieces together from the team

Interesting:

- different interpretations: 1. Lc: just start writing code, move forward vs. 2. wait and explain for better understanding
- Jo: Doing **is** Learning
- Jo: Since we're not working on production code - this helps in focusing on hands-on learning
- Jc: Expect code to start off imperfect, that's what refactoring is for
- Agree on this: instead of talking, write code - bias to action
- Also - expect less from the code at first, doesn't need to be perfect
- Pseudo-code for shared understanding - lowers the expectation for perfection
- Having a variety of perspectives about the events, we're focusing on different aspects of the contributing process. E.g. Susan broke down the structural pieces of what we'e built - te specifics of what we did, and in contrast Joss said "did coding", focusing more about the "Why?" (not the "What?")

Strong Emotions

- I rarely understand at the beginning - but, we can figure it out as an ensemble as we go; when we get to the end, it makes better sense; can still make progress as a Talker by focusing on the intent of the previous Talker.
- Used to not knowing anything; This is a safe place

- Nitsan Enjoys sessions where we get on the same page. This will make the next session faster. Now we all understand the goal.

- Felt like the tooling got in the way when working on approvaltests in gitpod. We don't know who will see editors that pop up. Didn't have intellisense or copilot. 
- We can make this better, but 

- Having timer be our next role is helpful
  - Having the typist start the timer is more transparent
  - Less requirements on norms

- Worry - We've added an openai dependency that won't work on CI.  Need an openai api key to work
  - Can be fixed easily 

- 

Changes:

- Bias to Action: just start writing the code, BUT we don't expect this code to be good; as Arlo says "perfect is the enemy of good, but good is the enemy of slightly less terrible"; so let's aim for terrible, but it'll show us the direction to go forward
- Experiment: having the typist start the timer