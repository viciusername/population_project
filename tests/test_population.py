import pytest
from population_sort import sort_by_area, sort_by_population


@pytest.fixture
def sample_data():
    return [
        ("Країна A", 100000, 5000000),
        ("Країна B", 200000, 3000000),
        ("Країна C", 150000, 7000000),
    ]


@pytest.mark.parametrize(
    "func,expected",
    [
        (
            sort_by_area,
            [
                ("Країна B", 200000, 3000000),
                ("Країна C", 150000, 7000000),
                ("Країна A", 100000, 5000000),
            ],
        ),
        (
            sort_by_population,
            [
                ("Країна C", 150000, 7000000),
                ("Країна A", 100000, 5000000),
                ("Країна B", 200000, 3000000),
            ],
        ),
    ],
)
def test_sorting_functions(sample_data, func, expected):
    assert func(sample_data) == expected
