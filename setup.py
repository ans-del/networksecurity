from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements

    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:

            # read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print("requiremets.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Anshika Saroj",
    author_email="anshikasaroj139@gmai.com",
    packages=find_packages(),
    installrequire=get_requirements()
)

## this is the basic file to setup a file

