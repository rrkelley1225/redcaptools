import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="redcaptools",
    version="0.1.0",
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    author="Robert Kelley",
    author_email="rob@r2klabs.com",
    description="A package for interfacing with a REDCap Instance",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rrkelley1225/redcaptools",
    packages=setuptools.find_packages(),
    install_requires=[
          'pycurl', 'io', 'urllib', 'json', 'pandas'
    ],
    include_package_data=True,
    zip_safe=False)