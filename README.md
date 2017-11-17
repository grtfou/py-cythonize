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
$ python -m unittest tests/run_tests.py
.
----------------------------------------------------------------------
Ran 2 tests in 0.063s

OK
```
