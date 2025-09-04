#! /bin/sh

python setup/setup.minimal.py sdist bdist_wheel
twine upload --repository-url ${TWINE_REPOSITORY_URL} dist/*
rm -r dist
