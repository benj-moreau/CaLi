from setuptools import setup

setup(name='cali',
      version='0.1',
      description='Defines a partial order over licenses',
      url='https://github.com/benjimor/CaLi',
      author='benjimor',
      author_email='benjimor44@gmail.com',
      license='MIT',
      packages=['cali'],
      install_requires=[
          'rdflib',
      ],
      zip_safe=False)
