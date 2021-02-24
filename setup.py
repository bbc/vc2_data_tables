import os

from setuptools import setup, find_packages

version_file = os.path.join(
    os.path.dirname(__file__),
    "vc2_data_tables",
    "version.py",
)
with open(version_file, "r") as f:
    exec(f.read())

setup(
    name="vc2_data_tables",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/bbc/vc2_data_tables",
    author="BBC R&D",
    description="Machine-readable constants and data tables for the SMPTE ST 2042-1 VC-2 professional video codec.",
    license="GPLv2",
    classifiers=[
        "Development Status :: 3 - Alpha",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",

        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",

        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    keywords="vc2 dirac dirac-pro constants data-tables quantisation-matrix",
    install_requires=["enum34; python_version < '3.4'"],
    entry_points = {
        'console_scripts': [],
    },
)
