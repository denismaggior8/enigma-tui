from setuptools import setup, find_packages
from pathlib import Path


this_directory = Path(__file__).parent
long_description = (this_directory/".."/".."/"README.md").read_text()


setup(
    author="Denis Maggiorotto",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/denismaggior8/enigma-tui",
    name="enigmatui",
    version="1.1.1-rc1",
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