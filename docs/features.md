# Features

<!-- toc -->
## Contents

    * [Verify(text) ensures a newline at the file](#verifytext-ensures-a-newline-at-the-file)
      * [Upgrade Path](#upgrade-path)
    * [Namer handles multiple nested methods in a unit test](#namer-handles-multiple-nested-methods-in-a-unit-test)
  * [v 0.5.0](#v-050)
    * [Options - with file extension](#options---with-file-extension)<!-- endToc -->
## v 1.0.0 
### Verify(text) ensures a newline at the file
**BREAKING CHANGE**
Since most tools will ensure a newline at the end of a file, approval test is now
adding this to allow copying approval results in diff tools to work correctly.
Please note that this will break all you previous approvals that do *not* end with
a newline!

This will show by your diff tool opening with two files that look identical, but
one actually has a newline at the end.

#### Upgrade Path
We suggest you use `ReporterByCopyMoveCommandForEverythingToClipboard()` as your [Default Reporter]() to re-approve all your files.

### Namer handles multiple nested methods in a unit test
Previously if you had nested methods in your unit test, the names would incorrectly
identify the help method rather than the test method. This is now fixed.

## v 0.5.0
### Options - with file extension
If you want to set the extension of the approval file, you can now do it through the options.

<!-- snippet: options_with_file_extension -->
<a id='snippet-options_with_file_extension'></a>
```py
verify(content, options=Options().for_file.with_extension(".md"))
```
<sup><a href='/tests/test_options.py#L56-L58' title='Snippet source file'>snippet source</a> | <a href='#snippet-options_with_file_extension' title='Start of snippet'>anchor</a></sup>
<!-- endSnippet -->
