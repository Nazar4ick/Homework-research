from distutils.core import setup


setup(
    name='economic_analysis',
    packages=['economic_analysis'],
    version='0.0.1',
    description='Program for economic indicators visualization',
    author='Nazar Mamonov',
    author_email='mamonov@ucu.edu.ua',
    requires=['matplotlib', 'json', 'ctypes', 'urllib.request'],
    url='https://github.com/Nazar4ick/Homework-research',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Economics"
        ],
    long_description="""\
Economic analysis helper
-------------------------------------

This program helps analysing major macroeconomic indicators by: 
-searching them
-visualizing them

This version requires Python 3 or later.
""",
)
