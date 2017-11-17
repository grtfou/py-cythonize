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
import shutil
from setuptools import setup
from setuptools.extension import Extension
from distutils.command.clean import clean

from Cython.Build import cythonize
from Cython.Distutils import build_ext

import yaml


settings = {}
try:
    with open('project_setting.yaml', 'r') as iif:
        settings = yaml.load(iif)
except FileNotFoundError:
    print('Please create "project_setting.yaml" and give settings.')
except (yaml.scanner.ScannerError):
    print('Please check your YAML format.')

mypj = settings.get('project_name', 'no-project-name')


class Clean(clean):
    """
    Delete all compile files.

    How to:
        $ python cythonize_pycode.py clean
    """

    def run(self):
        clean.run(self)

        for subdir in (mypj,):
            root = os.path.join(os.path.dirname(__file__), subdir)
            for dirname, dirs, _ in os.walk(root):
                for fn in glob.glob('{0}/*.py[ocx]'.format(dirname)):
                    os.remove(fn)
                for fn in glob.glob('{0}/*.c'.format(dirname)):
                    os.remove(fn)
                for fn in glob.glob('{0}/*.so'.format(dirname)):
                    os.remove(fn)
                for dn in dirs:
                    if dn == '__pycache__':
                        shutil.rmtree(os.path.join(dirname, dn))


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
                '/'.join(entry.split('/')[1:]), entry.split('/')[-1]
                # entry[2:], entry[2:].split('/')[-1]
            ))

    return dirs_name


def _build_so():
    """
    Building all python code to Cython code.
    """
    module_list = []
    sources = []
    root_module_name = mypj
    black_list = ['tests']

    for dirname in _get_dirs():
        path = dirname[0]
        if path.split('/')[0] in black_list:
            continue

        if _is_exist_pyfile(path):
            # sources.append(path.rstrip('/') + '/*.py')
            sources = [path.rstrip('/') + '/*.py']
            module_name = "{}.*".format(root_module_name)

            print('=' * 30)
            print(sources)
            print(module_name)
            print('=' * 30)
            module_list.append(
                Extension(
                    module_name,
                    sources=sources,
                    language='c'
                )
            )

    return module_list


class MyBuildCode(build_ext):
    """
    Customizition build script if it needs.
    """
    pass


if __name__ == '__main__':
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
        cmdclass={
            'clean': Clean,
            'build_ext': MyBuildCode
        },
        test_suite="tests.run_tests",
        # packages=[""]
    )
