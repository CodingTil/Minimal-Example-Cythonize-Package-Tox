import pathlib

from setuptools import setup
from Cython.Build import cythonize

# The directory containing this file
HERE = pathlib.Path(__file__).parent.resolve()

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="minimal_example",
    version="1.0.0",
    description="minimal_example",
    classifiers=[
        "Programming Language :: Python :: 3.10",
    ],
    packages=["mypackage_name"],
    include_package_data=True,
    install_requires=[
        "Cython>=0.29.21"
    ],
    ext_modules=cythonize("mypackage_name/*.py"),
)
