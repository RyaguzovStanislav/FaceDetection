from setuptools import setup, find_packages

import detection

# python setup.py bdist_wheel [--dist-dir=<...>]
# python setup.py bdist_wheel --dist-dir="distribution"

build_version = detection.__version__

platform = 'any'


def get_long_description():
    with open('README.txt', encoding='UTF-8') as f:
        result = f.read()
    return result


def install_requires():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    if "linux" in platform.lower():
        with open('requirements.txt') as f:
            requirements += f.read().splitlines()
    return requirements


setup(
    name='detection',
    mainteiner='DATA',
    mainteiner_email='admin@data.com',
    version=build_version,
    description='detection - пакеты и модули механизма детекции лиц на фото',
    long_description=get_long_description(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires(),
    python_requires='>=3.8',
    options={'bdist_wheel': {'plat_name': platform}}
)
