"""
Use Cython to cythonize the project.

Command:
  * $ python cythonize_pycode.py build_ext --inplace
  * $ python cythonize_pycode.py bdist_wheel

Ref:
  * http://cython.readthedocs.io/en/latest/index.html
  * https://docs.python.org/dev/distutils/apiref.html
"""
import os
import glob
import random
from setuptools import setup
from setuptools.extension import Extension

from Cython.Build import cythonize
from Cython.Distutils import build_ext

import yaml


def _is_exist_pyfile(path='.'):
    """
    Checking python code in the directory.
    """
    # If the directory has 'ignore' file. skip it.
    for entry in glob.glob(path + '/ignore'):
        return False

    for entry in glob.glob(path + '/*.py'):
        return True

    return False


def _get_dirs(path='.'):
    """
    Getting all modules name (directories name).
    """
    dirs_name = []
    for entry in glob.glob(path + '/**', recursive=True):
        if os.path.isdir(entry):
            dirs_name.append((
                entry[2:], entry[2:].split('/')[-1]
            ))

    return dirs_name


def _build_so():
    """
    Building all python code to Cython code.
    """
    module_list = []
    for dirname in _get_dirs():
        path = dirname[0]
        dn = dirname[1]

        if _is_exist_pyfile(path):
            sources = [path + '/*.py']
            module_list.append(
                Extension(
                    "{}.*".format(dn),
                    sources=sources,
                    language=random.choice(['c', 'c++']),
                )
            )

    return module_list


class MyBuildCode(build_ext):
    """
    Customizition build script if it needs.
    """
    pass


if __name__ == '__main__':
    settings = {}
    try:
        with open('project_setting.yaml', 'r') as iif:
            settings = yaml.load(iif)
    except FileNotFoundError:
        print('Please create "project_setting.yaml" and give settings.')
    except (yaml.scanner.ScannerError):
        print('Please check your YAML format.')

    setup(
        name=settings.get('project_name', 'no-project-name'),
        version=settings.get('version', '0.0.0'),
        description=settings.get('desc', ''),
        author=settings.get('author', ''),
        ext_modules=cythonize(
            _build_so(),
            build_dir="build",
            compiler_directives=dict(
                always_allow_keywords=True
            )),
        cmdclass=dict(
            build_ext=MyBuildCode
        ),
        test_suite="tests.run_tests",
    )
