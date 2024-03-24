# Options

<!-- toc -->
## Contents

  * [Configuriation for verify](#configuriation-for-verify)
  * [Inline Approvals](#inline-approvals)
    * [Known Issues](#known-issues)<!-- endToc -->

## Configuriation for verify
All verify methods take an optional options parameter. This allows you to configure 
* The reporter
* Scrubbers
* file extensions


## Inline Approvals

### Known Issues

* Pycharm automatically removes trailing whitespace, which can cause the approval file to be different from the actual output.  
  * To disable this behavior go to:
  * File -> Settings -> Editor -> General -> On Save -> [ ] Remove trailing spaces
