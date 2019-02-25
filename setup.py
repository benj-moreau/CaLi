import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='pycali',
                 version='1.0',
                 description='A python package that defines a partial order over RDF licenses',
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
