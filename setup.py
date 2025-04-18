from setuptools import find_packages, setup
from typing import List


def get_requirements(filepath: str) -> List[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace('\n', '') for i in requirements]
    return requirements


setup(
    name="qasystem",
    version="0.0.1",
    description="Machine Learning Pipeline Project Structure",
    author="Mayukh Haldar",
    author_email="mayukhhaldar1@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
