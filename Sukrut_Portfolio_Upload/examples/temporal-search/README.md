# Temporal pattern search example

This small educational example illustrates temporal-window search using entirely
synthetic daily observations. It is not the SMARTER codebase, a reproduction of
the ICHI paper, or evidence of clinical performance. The data have no physical units.

## Run

Requires Python 3.10 or newer. No external packages or network access are needed.

```bash
python search_patterns.py
```

The script reads the adjacent CSV, scans seven-observation windows and ranks
eligible windows by Euclidean distance to a normalized query pattern.
It accepts six or seven observed values, fills at most one interior gap by linear
interpolation, and skips constant windows. The fixture is regularly sampled daily;
the script does not resample irregular dates.

## Expected behavior

The windows starting 2026-01-01 and 2026-01-15 have distance zero: they have the
same shape but different levels. Constant windows and windows with two missing
observations are excluded. See expected_output.txt for the complete sample output.

## Design choices and limitations

Window-level normalization here intentionally removes absolute level. The main
research library uses site-level normalization; do not substitute this example
for its methods. Adjacent results may overlap. This simple exhaustive search is
for a small illustration, not a performance benchmark or scalable retrieval engine.
