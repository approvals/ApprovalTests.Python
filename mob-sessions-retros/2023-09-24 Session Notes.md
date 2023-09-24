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


