#!/usr/bin/env python
from setuptools import setup, find_packages


setup(name='pysoup',
      version='0.1.1',
      description='Package management in a bowl',
      author='Roy Sommer',
      url='https://www.github.com/illberoy/pysoup',
<<<<<<< HEAD
      download_url='https://github.com/illberoy/pysoup/tarball/0.1.1',
=======
      download_url='https://github.com/illberoy/pysoup/tarball/0.1.0',
>>>>>>> master
      packages=find_packages(),
      include_package_data=True,
      scripts=['soup.py'],
      install_requires=['Twisted==15.5.0', 'blessings==1.6.0', 'PyYAML==3.11', 'argcomplete==1.0.0'],
      entry_points={'console_scripts': ['soup = soup:main']})
