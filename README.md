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
$ pip install dist/my_test_zoo-1.0.0-cp37-cp37m-macosx_10_15_x86_64.whl

$ cd ..
$ python run_tests.py
OR
$ python -m unittest run_tests.py
get Coffee
.Hello. 2020-11-27 07:25:36.025461
.
----------------------------------------------------------------------
Ran 2 tests in 0.424s

OK
```

$ pip freeze|grep my-test-zoo
$ pip
