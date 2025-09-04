#! /bin/sh

python setup/setup.minimal.py sdist bdist_wheel
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
rm -r dist
