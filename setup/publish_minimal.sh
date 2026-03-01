#!/bin/sh

cp setup/setup.minimal.py setup.py
python -m build .
rm setup.py
twine upload --repository-url ${TWINE_REPOSITORY_URL} dist/*
rm -r dist
