# Configuration
toc 

You can create directory level configuration for approvals.
To do this create a file named 'approvaltests_config.json' and place it in the same directory as your test.
As of right now, the only configuration that you can do is to add subdirectories where the approved and received files will show up.
There is nothing that you need to do in the tests themselves to use this.

## Samples

You can find a [sample configuration here](/tests/configuration/approvaltests_config.json) and a [sample test that uses it here](/tests/configuration/test_subdirectory.py).

## Examples

A sample approvaltests_config.json:

```
{
  "subdirectory": "approved_files"
}
```

## How to configure a default reporter for your system

If you don't like the standard default for reporting and wish to change it everywhere this is the recommended way to do it.

snippet: default_reporter

The problem is you need to do this before you do anything else.
While some test frameworks allow for this, our recommended suggestion is to do it directly in Python by using the `__init__.py`
below. 

**note:** Please be aware that this will not override the reporters that are specified in your tests, as approval tests uses
[the principle of least surprise.](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)

snippet: configure_approvaltests_under_init

snippet: configure_approvaltests



