import codecs
import sys
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Shortcut for building/publishing to Pypi
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel upload')
    sys.exit()


def parse_reqs(req_path='./requirements.txt'):
    """Recursively parse requirements from nested pip files."""
    install_requires = []
    with codecs.open(req_path, 'r') as handle:
        # remove comments and empty lines
        lines = (line.strip() for line in handle
                 if line.strip() and not line.startswith('#'))

        for line in lines:
            # check for nested requirements files
            if line.startswith('-r'):
                # recursively call this function
                install_requires += parse_reqs(req_path=line[3:])

            else:
                # add the line as a new requirement
                install_requires.append(line)

    return install_requires
    
# For making things look nice on pypi:
long_description = 'Python implemetation of the interval tree.'

setup(name='interval_tree',
    version='0.3.3',
    description='Python implemetation of the interval tree',
    author = 'Mans Magnusson',
    author_email = 'mans.magnusson@scilifelab.se',
    url = 'http://github.com/moonso/interval_tree',
    license = 'MIT License',
    install_requires=parse_reqs(),
    
    packages = [
        'interval_tree'
    ],
    keywords = [
        'interval tree'
    ],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    long_description = long_description,
)