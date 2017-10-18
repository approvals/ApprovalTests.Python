# ApprovalTests.Python

Capturing Human Intelligence - ApprovalTests is an open source assertion/verification library to aid testing.  
`approvaltests` is the ApprovalTests port for Python.

For more information see: [www.approvaltests.com](http://approvaltests.com/).

[![Build Status](https://travis-ci.org/approvals/ApprovalTests.Python.png?branch=master)](https://travis-ci.org/approvals/ApprovalsTests.Python)

## What can I use ApprovalTests for?

You can use ApprovalTests to verify objects that require more than a simple assert including long strings, large arrays, 
and complex hash structures and objects.  ApprovalTests really shines when you need a more granular look at the test 
failure.  Sometimes, trying to find a small difference in a long string printed to STDOUT is just too hard!  
ApprovalTests solves this problem by providing reporters which let you view the test results in one of many popular diff 
utilities.

## SETUP

From pypi:

	pip install approvaltests

## GETTING STARTED

```python

    import unittest
    
    from approvaltests.approvals import verify
    from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory
    
    
    class GettingStartedTest(unittest.TestCase):
        def setUp(self):
            self.reporter = GenericDiffReporterFactory().get_first_working()
    
        def test_simple(self):
            verify('Hello', self.reporter)
    
    if __name__ == "__main__":
        unittest.main()
```

Approvals work by comparing the test results to a golden master.  If no golden master exists you can create a snapshot 
of the current test results and use that as the golden master.  The reporter helps you manage the golden master.  
Whenever your current results differ from the golden master, the reporter will launch an external application and then 
change some part of the system.  Either you will update the master because you expected the changes and they are good,
or you will go back to your code and update or roll back your changes to get your results back in line with the 
golden master.

The reporter is used both to alert you to changes in your test output, and to provide a tool to update the golden 
master.  So, diff and merge utilities make very good reporters.  Approvals come with a few reporters configured, 
supporting Linux, Mac OSX, and Windows.  In the example shown above, we use the `GenericDiffReporterFactory` to find 
and select the first diff utility that exists on our system.  Later, we pass that reporter to the verify method so that
it can be used if the test fails.

You don't have to do it this way.  You can request a specific reporter from the factory using the `get` method

```python    
    class GettingStartedTest(unittest.TestCase):
        def setUp(self):
            self.factory = GenericDiffReporterFactory()
    
        def test_simple(self):
            verify('Hello', self.factory.get('BeyondCompare4'))
```

Or you can build your own GenericDiffReporter on the fly

```python    
    class GettingStartedTest(unittest.TestCase):
        def test_simple(self):
            verify('Hello', GenericDiffReporter(('Custom', 'C:/my/favorite/diff/utility.exe')))
```

As long as `C:/my/favorite/diff/utility.exe` can be invoked from the command line using the format `utility.exe file1 file2` 
then it will be compatible with GenericDiffReporter.  Otherwise you will have to derive your own reporter, which 
we won't cover here.

To wrap up things up, I should note that you can completely replace the collection of reporters known to the reporter 
factory by writing your own JSON file and loading it.

For example if you had `C:/myreporters.json`

```json
[
    [
        "BeyondCompare4",
        "C:/Program Files (x86)/Beyond Compare 4/BCompare.exe"
    ],
    [
        "WinMerge",
        "C:/Program Files (x86)/WinMerge/WinMergeU.exe"
    ],
    [
        "Tortoise",
        "C:/Program Files (x86)/TortoiseSVN/bin/tortoisemerge.exe"
    ]
]
```

You could then use that file by loading it into the factory:

```python

    import unittest
    
    from approvaltests.approvals import verify
    from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory
    
    
    class GettingStartedTest(unittest.TestCase):
        def setUp(self):
            factory = GenericDiffReporterFactory()
            factory.load('C:/myreporters.json')
            self.reporter = factory.get_first_working()
    
        def test_simple(self):
            verify('Hello', self.reporter)
    
    if __name__ == "__main__":
        unittest.main()
```

Of course, if you have some interesting new reporters in `myreporters.json` then please consider updating the 
`reporters.json` file that ships with Approvals and submitting a pull request.


## SUPPORT AND DOCUMENTATION

* [Documentation](/docs/README.md)

* GitHub: [https://github.com/approvals/ApprovalTests.Python](https://github.com/approvals/ApprovalTests.Python)

* ApprovalTests Homepage: [http://www.approvaltests.com](http://www.approvaltests.com)
