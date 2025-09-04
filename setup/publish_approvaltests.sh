#! /bin/sh

python setup/setup.publish.py sdist bdist_wheel
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
rm -r dist
