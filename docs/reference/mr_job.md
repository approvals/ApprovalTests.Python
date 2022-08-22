#Testing MRJobs

toc

## Testing Single Job

Here's an example of how to test a single MRJob

snippet: verify_map_reduce

This will produce

snippet: test_mrjob.test_word_count.approved.txt

## Testing for a combination of inputs

If you want to test a combination of inputs against a job, you will need to create both a list of input values and a function that puts them together in to your data set.

Here's an example:

snippet: verify_templated_map_reduce

[Click here to see the results](../../tests/mrjob/test_mrjob.test_word_count_combinations.approved.txt)