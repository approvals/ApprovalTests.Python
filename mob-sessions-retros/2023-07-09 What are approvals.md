# 2022-07-09

==========

# Goals

-   improve documentation: explain better what approval tests mean
-   to that end, we're practicing using the fizzbuzz kata -> shared understanding -> document
-   idea: choose your own adventure documentation

# retro of the fizz buzz kata

-   timer could have been longer, maybe 5m
-   no typist recap
-   approving incorrect results - confusing, but it works, useful; one of many workflow with approvals
-   because we approved, we were able to safely refactor the code - e.g. extracting the `fizzbuzz` function
-   event - after extracting fizzbuzz - we got `None` - was easy to find that out thanks to the test; and the very short feedback loop (incl running the tests in watch mode)

what is "approval tests"?

-   it _is_ the feedback loop; the ability to get the FB from what you're doing, how changes affect output, w/o having to re-run it all the time
-   `verify` - compare the result to the approved file
    -   matches perfectly - test passes
    -   difference - the reporter highlights the mismatch; test fails
        -   textual representation of what we're working on

what does the user need to do, in order to use approvals?

-   setup a test
-   optional - reporter
-   do we need to create the approved file ourselves?
    -   initially it's created automatically when we first run the test
    -   once we receive a result that we like - we alter the approved file to reflect this - iow we copy received to approved

# Overall Retro

```
Approvals Retro
	team
		new member
			fresh eyes
				Beginners Mind
					Book about Zen
						Be as stupid as possible is good
		being open to attempt to answer guiding questions is a great attitude
	emotions
		positive impression
		very happy to have a new person
		interresting
			wanted to jump in but didnt
				following what is going on and checking whether I can understand to get feedback on where I am
				more comfortable to observe and assess my own understanding
				didnt want the others to change the process for me
					wanted to watch the others be in their flow
				participating vs observing
					like a little bit of both
		impressed with the courage of a new member to join
	tools
		gitpod
			reporter was not working the way we expected anymore
				the diff was not opening automatically
					we had to manually change the reporter
						could be a todo
			worked well, i liked it
			I dont know where the notes are
			had to change screensharing on every rotation
				idea: rotate typist slower
				idea: open gitpod in a teamviewer
		github code spaces (we didnt use it but one person tried it recently)
			idea: vscode liveshare
				to avoid having to screenshare
					need to try
	language
		python
			ternary way to write if else if else if else if, but you cannot add line breaks
	patterns
		first try a kata together to create a common understanding of what we want to document
	events
		one person delaying thumb vote answers and then giving the only thumb down
			reminds me about the movie: twelve angry men
	domain
		for someone who is a full beginner (walking up the street) the documentation is not full enough to make sense of it
			they wouldnt know where to go to learn about unit testing, tdd or so
	surprises
		approve incorrect results on purpose
			highlight the changes in behaviour you are making
			the "orange state" (related, but not exactly it)
			if you commit and push, it looks as if it was correct, but its not
			but developing it like this was useful
	learned
		got a greater understanding of how the workflow actually happens (working with approvals)
			i knew it did that, but didnt know exactly how
				now I know
		python ternary if else
```

## chat gpt summary

https://chat.openai.com/share/cb8855c9-c902-4b33-a2ce-32f6dfdb2b8c
