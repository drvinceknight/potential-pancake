from setuptools import find_packages, setup

# Read in the requirements.txt file
with open("requirements.txt") as f:
    requirements = []
    for library in f.read().splitlines():
        requirements.append(library)

setup(
    name="csv_data_explorer",
    install_requires=requirements,
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="",
)
