from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="awaits",
    version="0.0.1",
    author="Evgeniy Blinov",
    author_email="zheni-b@yandex.ru",
    description="async + threads + decorators = ?",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/pomponchik/awaits",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
)
