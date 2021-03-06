from setuptools import setup, find_namespace_packages

setup(
    name="WeatherLookup",
    long_description="""
Lookup the live weather data to any city!

## Valid Queries

- City name 
- State name
- Zipcode


## Installation

``` Bash
pip install WeatherLookup
```

## Usage 

```Python
import WeatherLookup

DubaiWeather = WeatherLookup.temperature('Dubai')
print(DubaiWeather)

```

```Python
import WeatherLookup

DubaiCondition = WeatherLookup.condition('Dubai')
print(DubaiCondition)

```""",
    long_description_content_type='text/markdown',
    version="1.0.2",
    description="Look up live weather data from across the world",
    author="Mustafa A",
    url="https://github.com/mustafaisnotsmart/WeatherLibrary",
    license="MIT",
    packages=find_namespace_packages(include="WeatherLookup.*"),
    install_requires=[
        "requests",
    ],
)