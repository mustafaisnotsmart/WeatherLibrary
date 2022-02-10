from setuptools import setup, find_namespace_packages

setup(
    name="WeatherLookup",
    version="1.0.0",
    description="Look up live weather data from across the world",
    author="Mustafa A",
    url="https://github.com/mustafaisnotsmart/WeatherLibrary",
    license="MIT",
    packages=find_namespace_packages(include="WeatherLookup.*"),
    install_requires=[
        "requests",
    ],
)