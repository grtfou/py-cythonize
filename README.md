# py-cythonize
Use Cython to cythonize the project.

```bash
$ copy cythonize_pycode.py <your_project_root_path>
$ vim  <your_project_root_path>/project_setting.yaml

$ python cythonize_pycode.py bdist_wheel

$ pip install dist/<your_project_name ...>.whl
# Then.. Enjoy it
```

## Unit Test

```bash
$ cp cythonize_pycode.py tests/
$ cd tests
$ python cythonize_pycode.py bdist_wheel
$ pip install dist/my_test_zoo-0.0-cp36-cp36m-macosx_10_12_x86_64.whl

$ python -m unittest run_tests.py
.
----------------------------------------------------------------------
Ran 2 tests in 0.063s

OK
```
