from setuptools import find_packages, setup

setup(
    name="titanic_kaggle",
    packages=find_packages(exclude=["titanic_kaggle_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
