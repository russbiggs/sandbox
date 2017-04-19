from setuptools import setup

setup(name='sandbox',
      version='0.1',
      description='creates temporary file for testing in VSCode',
      url='http://github.com/russbiggs/sandbox',
      author='Russ Biggs',
      author_email='russbiggs@gmail.com',
      license='MIT',
      packages=['sandbox'],
      install_requires=[],
      entry_points={
          'console_scripts': ['sandbox=sandbox.__main__:main'],
      },
      zip_safe=False)
