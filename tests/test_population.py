import pytest
from population_sort import read_population_data, sort_by_area, sort_by_population

@pytest.fixture
def sample_data():
    return [
        ("Країна A", 1000000, 50000000),
        ("Країна B", 2000000, 30000000),
        ("Країна C", 1500000, 70000000)
    ]

@pytest.mark.parametrize("func,expected", [
    (sort_by_area, [("Країна B", 2000000, 30000000), ("Країна C", 1500000, 70000000), ("Країна A", 1000000, 50000000)]),
    (sort_by_population, [("Країна C", 1500000, 70000000), ("Країна A", 1000000, 50000000), ("Країна B", 2000000, 30000000)])
])
def test_sorting_functions(sample_data, func, expected):
    assert func(sample_data) == expected
