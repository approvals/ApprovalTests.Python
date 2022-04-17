## Via Github Actions
1. Change version number in 
https://github.com/approvals/ApprovalTests.Python/blob/master/approvaltests/version.py

2. Create a new realease with that version number and tag it. 
https://github.com/approvals/ApprovalTests.Python/releases

Done! it will automatically push to pypi via the github action.

## From personal Machine (historical)
### Prerequisites

* An account on pypi and pypitest
* Access to approvaltests on pypip and pypitest
* a `.pypirc` file in your home dir, e.g.

```
[distutils]
index-servers =
    pypi
    pypitest

[pypi]
username: your_username
password:


[pypitest]
username: your_username
password:
```

### Pushing a new version to pypi

Increment version in approvaltests/version.py.

 ```bash
$  git tag 0.1.13 -m "Adds new reporters and dynamic way to find test name"
$  git push --tags origin master

$  python setup.py sdist upload -r pypitest
# should be deployed at: https://testpypi.python.org/pypi
  
$  python setup.py sdist upload -r pypi
# should be deployed at: https://pypi.python.org/pypi
```
