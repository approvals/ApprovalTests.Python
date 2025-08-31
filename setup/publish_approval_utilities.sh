#!/bin/sh

mv setup/setup.py setup/setup.approvaltests.py
cp setup/setup.approval_utilities.py setup/setup.py
python setup/setup.py sdist bdist_wheel
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
rm setup/setup.py
mv setup/setup.approvaltests.py setup/setup.py
rm -r dist
