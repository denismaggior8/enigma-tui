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
    version="0.0.1",
    packages=find_packages(
        # All keyword arguments below are optional:
        where='.',  # '.' by default
        include=['enigmatui'],  # ['*'] by default
    ),
    description="Enigma TUI is a Terminal User Interface for Enigma machines, allowing you to simulate different Enigma machine models from the terminal"
)