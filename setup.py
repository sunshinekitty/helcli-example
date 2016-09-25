
from setuptools import setup, find_packages

with open("VERSION", "rt") as vfile:
    version = vfile.readline()

setup(name='helcli-example',
      version=version,
      author='Alex Edwards',
      author_email='edwards@linux.com',
      packages=find_packages(),
      install_requires=['helcli'],
      entry_points={'console_scripts': [
              'helcli = example:main',
          ]})

# vim:et:fdm=marker:sts=4:sw=4:ts=4
