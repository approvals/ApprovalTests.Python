There should be a way to still allow multiple `verify` per approved file for the rare

We created a way to throw an error when multiple verify calls are used in a single test

Still to do for our feature:
- allow users to suppress the exception explicitly
- allow users to use multiple verifys in a single test by suppressing said exception

## proposed solution

- option #1 - use the same approach that we used to throw the error, to turn on the capability to throw multiple verifies in a single test
- option #2 - use an environment variable
- option #3 - Use options
    - allow you to set global options that would take effect for your whole test suite
    - and the theory is: that would allow you to set this gloabally
    - CONCERN: we are not sure this will work the way we expect
- option #4 - use something like .with_context_manager 
- allow the user to use mulitpl verifies for one test, not for all of the verifies 
```python
with open('myfile.txt', 'r') as f:
  content = f.read()
  # Do something with the content...

# File is automatically closed outside the "with" block
```


we looked at this file: logging_approvals.py
and we notice that it is a different use case. 

logging does some work then calles verfy on the exit
and we want to allow the user to call verify themselves
so logging might be a good model 

Currently thinking:
a better design  might be to use options rather context manager.

## Retro

### How did that feel?

feels like been missing the mob
Enjoy the small group size, easier to keep track, engaged more often as Talking / Typing; Learning hands-on
Felt alright to get asked Qs, until it clicked

worried: about being domiminat in theis forum
reply: it is not about dominance it is appreciated because you <often> know how to fix it.
it is fine line between dominance and autocratic
leadership gives you info and allows you to do it.
I want the responsibility to be shared within hte team 
and I do not want too much of the responsibility in this TEAM setting
I try to get to share the responsibility somehow.
RESPONSE: i am worried that you are thinking people will preceive that you think that better than the others
that phrase is too broad
there are things I am probably better at than
i might have more experience in a specific scenario than another person.
that is not the worrry
am i taking too much space, I am allowing for shared responibility
i want  balanced responsibility 
if i want to be better, it is my reponsibility to work to become better
 and to know I can be as good as you
it is my responibility to apply myself

last week was a hell week for me.  I had peole dub for me and I was able to explain to them exactly what i needed from them. and I didnt realize that I have all the peices that I need
I adapt and I am doing OK, even if I don't feel like I am doing well, 

frustrations
- when we have some flow and direction, and shared understanding; even if we find it's a dead end - that feels good
- today were some points - when we're not holding that feeling (shared understanding) throughout a full rotation - this causes frustration
- J is encouraging D to focus on the technical and let go of the facilitation. D noticed that when they're able to focus on the 'technical' they can help the team keep the shared undersanding from the technical perspective.
- Something I'm trying to do in this mob, is to stop using my cognitive power to facilitate, and focus all of my cognitive power on the 'technical'
- but when focusing on losing flow / or anything distracts me - it's harder to hold the shared understaning from a technical perspective


### What worked well?

understood the process, need to understand the code better
explaining the reasons behind making changes
Emphasis on understanding rather than just doing; asking Qs about what and why. Helped me help others. 
on the cusp of understanding.  just a little bit more and you will realize that 
   ' I do understand'
at some undfined point you decide dfor yourself, now I do understand
 on the way there, there is a continuous learning
and at some point you realize I do understand
when does a person decide: I DO understand!
often they say: I do not udnerstand anything, 
and then suddenly they get it

the Ah ha moment is something I am very fond of.

Liked how everybody helps each other, with patience - believing and saying "you'll get there in the end"

### Observed
Nitsan asked Joss a leading question during retro. 
"did that feel ok to you"
more open ended question
"how did it feel when i did xyz"

- someone might consider that today was a failed expereiment:
- it might feel like it was no progress
- from Nitsans persepctive: 
- if we then decided that  it is not a good fit
- then THAT is OK,  it is for understanding and learning
- 

### Learned

### Idea

When feeling like I don't quite understand, then I might ask the group for help by saying - 
"Could somebody hold space form me to help me think this through?"
"Could you ask me Qs to help me comprehend this part of the code?"
EXAMple;
"I noticed some confustion on your expression"
may i ask you about it>
I explained the thing in my own words, then I aske dyou to repeate the explaination back to me
 and 
it was hard to repeat back so 
We noticed there might be a gap there (since it was hard to repeat back)
THen
  Helped orient the thinking
started with what are we working on
why?
what have we achieved up to now?
what is still missing?

Right before my next turn - try to focus on the current typing-talking pair - this helps in preserving the flow
