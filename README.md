# Set up environment

Create and activate a virtual env [Python Doc](https://docs.python.org/es/3/library/venv.html).

## Install dependencies

You will need the **environment activated**

- Run `pip install`

## Execute the tests

To execute all the tests
`pytest -s tests/`

To execute all the test in an specific module
`pytest -s tests/test_weather.py`

To execute an specific node
`pytest -s tests/test_weather.py::TestClass::test_weather_services`
