#! /bin/sh

python setup/setup.publish.py sdist bdist_wheel
twine upload --repository-url ${TWINE_REPOSITORY_URL} dist/*
rm -r dist
