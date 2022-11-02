from typing import List
from setuptools import find_packages , setup #find_packages : Return a list all Python packages found within directory 'where' is the root directory which will be searched for packages. We have create a folder sensor/package and it is going to search and install as lib.setup : create package

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    Returns:
        List[str]: requiremetns list
    """
    requirement_list:List[str]=[]
    # Code to read from requirements.txt file and append in requirement list.
    
    return requirement_list

setup(
    name="sensor",
    version="0.0.1",
    author="Divyanshu Kesarwani",
    author_email="kingsapp14@gmail.com",
    packages=find_packages(), # calling the function to search for the packages
    install_requires=get_requirements(),
    
)