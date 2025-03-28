from typing import List, Tuple


def read_population_data(file_path: str) -> List[Tuple[str, float, int]]:
    """Зчитує дані з файлу та повертає список (країна, площа, населення)."""
    data = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) != 3:
                continue

            country, area, population = parts
            try:
                country = country.strip()
                area = float(area.strip())
                population = int(population.strip())

                data.append((country, area, population))
            except ValueError:
                continue

    return data


def sort_by_area(
    data: List[Tuple[str, float, int]]
) -> List[Tuple[str, float, int]]:
    """Сортує список за площею (від більшого до меншого)."""
    return sorted(
        data,
        key=lambda x: x[1],
        reverse=True
    )


def sort_by_population(
    data: List[Tuple[str, float, int]]
) -> List[Tuple[str, float, int]]:
    """Сортує список за населенням (від більшого до меншого)."""
    return sorted(
        data,
        key=lambda x: x[2],
        reverse=True
    )
