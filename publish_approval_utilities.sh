#!/bin/sh

mv setup.py setup.approvaltests.py
cp setup.approval_utilities.py setup.py
python setup.py sdist bdist_wheel
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
rm setup.py
mv setup.approvaltests.py setup.py
rm -r dist
