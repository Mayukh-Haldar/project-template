from setuptools import find_packages, setup
from typing import List


def get_requirements(filepath: str) -> List[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace('\n', '') for i in requirements]
    return requirements


setup(
    name="name_of_your_project",
    version="version_of_your_project",
    description="project_description",
    author="your_name",
    author_email="your_email",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
