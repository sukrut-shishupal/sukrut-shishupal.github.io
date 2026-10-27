"""Small temporal similarity example using synthetic daily observations.

Educational demonstration, not the SMARTER extraction pipeline.
Python 3.10+; standard library only. Run from any directory.
"""
import csv
import math
from pathlib import Path

WINDOW = 7
QUERY = [2, 3, 5, 9, 5, 3, 2]


def normalize(values):
    """Normalize each example window, not the whole monitoring site."""
    mean = sum(values) / len(values)
    scale = math.sqrt(sum((x - mean) ** 2 for x in values) / len(values))
    if scale < 1e-12:
        return None  # Constant windows do not have a defined shape here.
    return [(x - mean) / scale for x in values]


def prepare(values):
    """Accept >=6/7 observed; interpolate one interior gap only."""
    missing = [i for i, x in enumerate(values) if x is None]
    if len(values) != WINDOW or len(missing) > 1:
        return None
    if missing and missing[0] in (0, WINDOW - 1):
        return None  # No extrapolation at the edges.
    filled = values.copy()
    if missing:
        i = missing[0]
        filled[i] = (filled[i - 1] + filled[i + 1]) / 2
    return normalize(filled)


def search(path):
    with path.open(newline='') as handle:
        records = list(csv.DictReader(handle))
    values = [float(r['synthetic_value']) if r['synthetic_value'] else None for r in records]
    if any(x is not None and not math.isfinite(x) for x in values):
        raise ValueError('Observed values must be finite')
    query = normalize(QUERY)
    matches = []
    for start in range(len(values) - WINDOW + 1):
        candidate = prepare(values[start:start + WINDOW])
        if candidate is None:
            continue
        distance = math.sqrt(sum((a - b) ** 2 for a, b in zip(query, candidate)))
        matches.append((distance, records[start]['date'], records[start + WINDOW - 1]['date']))
    return sorted(matches)


if __name__ == '__main__':
    source = Path(__file__).with_name('synthetic_daily.csv')
    matches = search(source)
    print('Synthetic illustration; lower distance means a closer normalized shape.')
    print(f'Eligible windows: {len(matches)}')
    for distance, start, end in matches[:5]:
        print(f'{start} to {end}: distance={distance:.6f}')
