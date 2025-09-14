## Python Style

if the external process means we should fail use check=True 
and let the exception bubble up

if the external process means we should continue use check=False
and handle the return code.

## Method length

Methods should be short and focused on a single responsibility.
Extract code paragraphs into seperate methods. Using a functional programming style whenever possible. Make the method names self explanatory.

Don't use comments that repeat what the code does. This includes docstrings.


## TypeHints

Use type hints on method parameters and return values.

## Path
Please use Pathlib everywhere.


## Os
to check the os, us platform.system()