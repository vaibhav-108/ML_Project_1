from setuptools import find_packages,setup

from typing import List

HYPHEN_DOT_E = '-e .'
def get_requirements(file_path:str)-> List[str]:
    '''
    This function will return the list of requirement
    '''
    requirements =[]
    with open(file_path,'r') as file_obj:
        requirements= file_obj.readlines()
        requirements =[req.replace('\n',"") for req in requirements]
        
        if HYPHEN_DOT_E in requirements:
            requirements.remove(HYPHEN_DOT_E)
        
        
    return requirements
        

    
setup(
    name='ML_project1',
    version='0.0.1',
    author='vaibhav',
    author_email='vaibhav.b108@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)

