from setuptools import setup, find_packages
from pathlib import Path
import os
import re


this_directory = Path(__file__).parent
long_description = (this_directory/".."/".."/"README.md").read_text()

def read_version():
    with open(os.path.join("enigmatui", "__init__.py")) as f:
        match = re.search(r'__version__\s*=\s*[\'"]([^\'"]+)[\'"]', f.read())
        if match:
            return match.group(1)
        raise RuntimeError("Unable to find version string.")


setup(
    author="Denis Maggiorotto",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/denismaggior8/enigma-tui",
    name="enigmatui",
    version=read_version(),  # Use a function to read the version from __init__.py
    include_package_data=True,
    packages=find_packages(
        # All keyword arguments below are optional:
        where='.',  # '.' by default
    ),
    include_dirs= ["css"],
    package_data={'enigmatui': ['css/*.css', 'css/*.css']},
    entry_points={
        "console_scripts": [
            "enigmatui = enigmatui.__main__:main",  # 
        ],
    },
    install_requires=[
        "textual==1.0.0",
        "enigmapython==1.2.3"
    ],
    description="Enigma TUI is a Terminal User Interface for Enigma machines, allowing you to simulate different Enigma machine models from the terminal"
)