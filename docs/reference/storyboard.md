# Storyboard

<!-- toc -->
## Contents

  * [Why Use Storyboards](#why-use-storyboards)
  * [How To Use Storyboards](#how-to-use-storyboards)
  * [verify_storyboard](#verify_storyboard)<!-- endToc -->

## Why Use Storyboards
 
Sometimes we might want to see different steps in a workflow or lifetime of an object. Storyboards are a convenience object to help enable that.

Approvaltests allows us to look at a complete object instead of just pieces of it. Storyboards allow us to track an object through time. 

The mechanism to map time to space that storyboards use is very analogous to a comic book, but with each frame vertically after each other so that it works well with the diff tool and shows a progression.

## How To Use Storyboards

Here is example of creating story board, adding content to it, and verifying it.

<!-- snippet: use_storyboard -->
<a id='snippet-use_storyboard'></a>
```py
story = Storyboard()
story.add_description("Spinning wheel")
story.add_frame(ascii_wheel)
ascii_wheel.advance()
story.add_frame(ascii_wheel)
verify(story)
```
<sup><a href='/tests/test_verify.py#L234-L241' title='Snippet source file'>snippet source</a> | <a href='#snippet-use_storyboard' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

will produce 

<!-- snippet: VerifyTests.test_simple_storyboard.approved.txt -->
<a id='snippet-VerifyTests.test_simple_storyboard.approved.txt'></a>
```txt
Spinning wheel

Initial:
-

Frame #1:
\
```
<sup><a href='/tests/approved_files/VerifyTests.test_simple_storyboard.approved.txt#L1-L8' title='Snippet source file'>snippet source</a> | <a href='#snippet-VerifyTests.test_simple_storyboard.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

## verify_storyboard

You can also use the `with verify_storyboard() as b:` syntax
which will verify the storyboard on context exit.
___
[Back to top](../README.md)
