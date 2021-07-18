# Storyboard

<!-- toc -->
## Contents

  * [Why Use Storyboards](#why-use-storyboards)
  * [How To Use Storyboards](#how-to-use-storyboards)
  * [How to Add multiple Frames](#how-to-add-multiple-frames)<!-- endToc -->

## Why Use Storyboards
 
 Sometime we might want to see different steps in a workflow or lifetime of an object. Storyboards enable that.

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
<sup><a href='/tests/test_verify.py#L155-L162' title='Snippet source file'>snippet source</a> | <a href='#snippet-use_storyboard' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

## How to Add multiple Frames
___
[Back to top](../README.md)
