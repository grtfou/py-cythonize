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
from setuptools import setup, find_packages
from setuptools.extension import Extension
from distutils.command.clean import clean
from distutils.command.build_py import build_py
from Cython.Build import cythonize

import yaml


settings = {}
try:
    with open('project_setting.yaml', 'r') as iif:
        settings = yaml.load(iif)
except FileNotFoundError:
    print('Please create "project_setting.yaml" and give settings.')
except (yaml.scanner.ScannerError):
    print('Please check your YAML format.')

MY_PROJ_PATH = settings.get("module_path", ".")
FULL_SETUP_DIRNAME = os.path.abspath(os.path.dirname(__file__))


class Clean(clean):
    """
    Delete all compile files.

    How to:
        $ python cythonize_pycode.py clean
    """

    def run(self):
        clean.run(self)

        for subdir in (MY_PROJ_PATH,):
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


class BuildCode(build_py):
    """
    Build cython files (.so)
    """

    def find_package_modules(self, package, package_dir):
        modules = build_py.find_package_modules(self, package, package_dir)
        for package, module, filename in modules:
            if module not in ('__init__',):
                continue
            yield package, module, filename


def find_ext_packages():
    ret = []
    for root, _, files in (os.walk(os.path.join(
                           FULL_SETUP_DIRNAME, MY_PROJ_PATH))):
        commonprefix = os.path.commonprefix([FULL_SETUP_DIRNAME, root])
        for filename in files:
            if not filename.endswith(('.py', '.c')):
                # no python or c code
                continue
            if filename in ('__init__.py',):
                # Block list
                continue
            full = os.path.join(root, filename)
            relpath = os.path.join(root, filename).split(commonprefix)[-1][1:]
            module = os.path.splitext(relpath)[0].replace(os.sep, '.')
            ret.append(Extension(module, [full]))
    return ret


if __name__ == '__main__':
    setup(
        name=settings.get('project_name', 'no-project-name'),
        version=settings.get('version', '0.0.0'),
        description=settings.get('desc', ''),
        author=settings.get('author', ''),
        ext_modules=cythonize(
            find_ext_packages(),
            build_dir="build",
            compiler_directives=dict(
                always_allow_keywords=True
            )),
        packages=find_packages(),
        cmdclass={
            'clean': Clean,
            'build_py': BuildCode
        },
        test_suite="tests.run_tests",
        # packages=[""]
    )
