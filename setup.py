import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='pycali',
                 version='0.1',
                 description='Defines a partial order over licenses',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url='https://github.com/benjimor/CaLi',
                 author='benjimor',
                 author_email='benjimor44@gmail.com',
                 license='MIT',
                 packages=setuptools.find_packages(),
                 install_requires=[
                     'rdflib',
                 ],
                 classifiers=[
                       "Programming Language :: Python :: 3",
                       "License :: OSI Approved :: MIT License",
                       "Operating System :: OS Independent",
                 ],
                 keywords=["license", "rdf", "semantic web", "research"],
                 )
