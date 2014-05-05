try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
# For making things look nice on pypi:
long_description = 'Python implemetation of the interval tree.'

setup(name='interval_tree',
    version='0.3.1',
    description='Python implemetation of the interval tree',
    author = 'Mans Magnusson',
    author_email = 'mans.magnusson@scilifelab.se',
    url = 'http://github.com/moonso/interval_tree',
    license = 'MIT License',
    install_requires=['pytest'],
    packages = ['interval_tree'],
    keywords = ['interval tree'],
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