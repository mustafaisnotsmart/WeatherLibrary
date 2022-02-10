from setuptools import setup, find_namespace_packages

setup(
    name="WeatherLookup",
    version="0.0.1",
    description="Look up live weather data from across the world",
    author="Mustafa A",
    url="https://www.github.com/RangerEmerald/NitrotypePy",
    license="MIT",
    packages=find_namespace_packages(include="weather-lookup.*"),
    install_requires=[
        "requests",
    ],
)