# Data Integrity Report

This repository treats agronomic catalog values as externally sourced facts.

## Truthfulness rules

- No fabricated catalog values.
- Missing fields remain null/unknown.
- Every stored attribute includes provenance fields: value + URL + evidence + hash + timestamp.

## Modeling boundaries

Simulation curves are synthetic and deterministic for demo reproducibility. They are not measured field performance.

## Limitations

- Source scrapers are disabled in this starter until full robots/ToS gate + rate limiter are implemented.
- Use manual import to attach verifiable provenance without violating source restrictions.
