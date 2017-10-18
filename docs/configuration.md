# Configuration

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
