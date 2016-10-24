 ```bash
$  git tag 0.1.13 -m "Adds new reporters and dynamic way to find test name"
$  git push tags origin master
$  git push --tags origin master

$  python setup.py sdist upload -r pypitest
# should be deployed at: https://testpypi.python.org/pypi
  
$  python setup.py sdist upload -r pypi
# should be deployed at: https://pypi.python.org/pypi
```
