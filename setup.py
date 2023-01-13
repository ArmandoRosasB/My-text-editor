from setuptools import setup

setup(
    name = 'Edit_tools',
    version= '1.0',
    description= 'Un paquete para realizar las funciones basicas de un editor de texto',
    author= 'Jose Armando Rosas Balderas',
    author_email= 'armando.rosas133@gmail.com',
    url= 'https://github.com/ArmandoRosasB',
    packages= ['Edit_tools', 'Edit_tools.file_editing'],
    scripts= ['text_editor.py']
)