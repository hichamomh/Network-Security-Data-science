'''
The setup.py file is an essential part of packaging and 
distributing Python projects. It is used by setuptools 
(or distutils in older Python versions) to define the configuration 
of your project, such as its metadata, dependencies, and more

'''

from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements 
    
    """
    requiremet_list:List[str] = []
    try:
        with open("requirements.txt","r") as file:
            # read lines from the file
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e.
                if requirement and requirement!="-e .":
                    requiremet_list.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requiremet_list

print(get_requirements())

setup(
    name="Network Security",
    version = "0.0.1",
    author="Hicham OUMOUHOU",
    author_email= "hichamoumouhou85@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)

