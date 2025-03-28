import pytest
from population_sort import read_population_data, sort_by_area, sort_by_population

@pytest.fixture
def sample_data():
    return [
        ("Країна А", 1000000, 5000000),
        ("Країна В", 2000000, 3000000),
        ("Країна С", 1500000, 7000000),
    ]

@pytest.mark.parametrize(
    "func,expected",
    [
        (sort_by_area, [
            ("Країна В", 2000000, 3000000),
            ("Країна С", 1500000, 7000000),
            ("Країна А", 1000000, 5000000),
        ]),
        (sort_by_population, [
            ("Країна С", 1500000, 7000000),
            ("Країна А", 1000000, 5000000),
            ("Країна В", 2000000, 3000000),
        ]),
    ]
)
def test_sorting_functions(sample_data, func, expected):
    assert func(sample_data) == expected
