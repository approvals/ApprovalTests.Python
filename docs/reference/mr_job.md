# Testing MRJobs

<!-- toc -->
## Contents

  * [What is MRJob](#what-is-mrjob)
  * [Testing Single Job](#testing-single-job)
  * [Testing for a combination of inputs](#testing-for-a-combination-of-inputs)<!-- endToc -->

## What is MRJob

[MRJob](https://mrjob.readthedocs.io/en/latest/) is a library to allow testing of Hadoop Map Reduce jobs. 
Map Redcue jobs take in data and transform it which makes it perfect for use with ApprovalTests.



## Testing Single Job

Here's an example of how to test a single MRJob

<!-- snippet: verify_map_reduce -->
<a id='snippet-verify_map_reduce'></a>
```py
def test_word_count() -> None:
    test_data = "one fish two fish red fish blue fish"
    map_reduction = MRWordFrequencyCount([])
    verify_map_reduce(map_reduction, test_data)
```
<sup><a href='/tests/mrjob/test_mrjob.py#L36-L43' title='Snippet source file'>snippet source</a> | <a href='#snippet-verify_map_reduce' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

This will produce

<!-- snippet: test_mrjob.test_word_count.approved.txt -->
<a id='snippet-test_mrjob.test_word_count.approved.txt'></a>
```txt
one fish two fish red fish blue fish

Map reduces to:

chars:36
lines:1
words:8
```
<sup><a href='/tests/mrjob/test_mrjob.test_word_count.approved.txt#L1-L7' title='Snippet source file'>snippet source</a> | <a href='#snippet-test_mrjob.test_word_count.approved.txt' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

## Testing for a combination of inputs

If you want to test a combination of inputs against a job, you will need to create both a list of input values and a function that puts them together in to your data set.

Here's an example:

<!-- snippet: verify_templated_map_reduce -->
<a id='snippet-verify_templated_map_reduce'></a>
```py
def test_word_count_combinations() -> None:
    animals = ["fish", "dog", "cat"]
    colors = ["aqua", "red", "blue"]
    map_reduction = MRWordFrequencyCount()

    def input_creator(animal: str, color1: str, color2: str) -> str:
        return f"one {animal} two {animal} {color1} {animal} {color2} {animal}"

    verify_templated_map_reduce(map_reduction, input_creator, [animals, colors, colors])
```
<sup><a href='/tests/mrjob/test_mrjob.py#L46-L58' title='Snippet source file'>snippet source</a> | <a href='#snippet-verify_templated_map_reduce' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->

[Click here to see the results](../../tests/mrjob/test_mrjob.test_word_count_combinations.approved.txt)
