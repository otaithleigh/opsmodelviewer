from setuptools import setup

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='opsmodelviewer',
    version='1.1.0',

    description='A viewer for 2D OpenSees models.',
    long_description=long_description,
    long_description_content_type='text/x-rst',

    package_dir={'': 'src'},
    py_modules=['opsmodelviewer'],
    entry_points={
        'console_scripts': ['opsmodelviewer = opsmodelviewer:main']
    },

    python_requires='>=3.6',
    install_requires=['bokeh>=1.4', 'pandas'],

    author='Peter Talley',
    author_email='ptalley2@vols.utk.edu',
    url='https://github.com/otaithleigh/opsmodelviewer',

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
)
