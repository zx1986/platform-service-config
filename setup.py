from setuptools import setup, find_packages
import pathlib

# Read the requirements from the requirements.txt file
here = pathlib.Path(__file__).parent.resolve()
with open(here / 'requirements.txt', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='platform_service_config',
    version='0.1.0',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.9',
    entry_points={
        'console_scripts': [
            'app=app.cli:cli',
        ],
    },
)
