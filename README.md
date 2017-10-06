# py-cythonize
Use Cython to cythonize the project.

```bash
$ copy cythonize_pycode.py <your_project_root_path>
$ vim  <your_project_root_path>/project_setting.yaml

$ python cythonize_pycode.py bdist_wheel

$ pip install dist/<your_project_name ...>.whl
# Enjoy it
```
