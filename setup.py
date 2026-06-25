# from setuptools import setup, find_packages
# from pathlib import Path


# def get_requirements(file_path: str):
#     requirements = Path(file_path).read_text().splitlines()

#     requirements = [
#         req.strip()
#         for req in requirements
#         if req.strip() and req.strip() != "-e ."
#     ]

#     return requirements


# setup(
#     name="Wine_Quality_Production",
#     version="0.0.1",
#     author="Rifat",
#     author_email="rifat.gameviz@gmail.com",
#     package_dir={"": "src"},
#     packages=find_packages(where="src"),
#     install_requires=get_requirements("requirements.txt"),
# )

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Wine_Quality_Production"
AUTHOR_USER_NAME = "Rifat"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "rifat.gameviz@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
