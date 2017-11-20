# py-cythonize
Use Cython to cythonize the project.

```bash
$ TARGET_PATH=<YOUR_PROJECT_ROOT_PATH>

$ cp cythonize_pycode.py $TARGET_PATH
$ cp project_setting.yaml $TARGET_PATH
$ cd $TARGET_PATH
$ vim project_setting.yaml

$ python cythonize_pycode.py bdist_wheel

$ pip install $TARGET_PATH/dist/<your_project_name ...>.whl
# Then.. Enjoy it
```

## Unit Test

```bash
$ cp cythonize_pycode.py tests/
$ cp project_setting.yaml tests/
$ cd tests
$ python cythonize_pycode.py bdist_wheel
$ pip install dist/my_test_zoo-0.0-cp36-cp36m-macosx_10_12_x86_64.whl

$ cd ..
$ python run_tests.py
OR
$ python -m unittest run_tests.py
.
----------------------------------------------------------------------
Ran 2 tests in 0.063s

OK
```
