python -m pip install --upgrade pip
pip install tox
pip install pytest 
tox -e py && tox -e test__py_typed_files_exist
