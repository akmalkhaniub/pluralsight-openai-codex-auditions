# AGENTS.md: Bookshop team rules

## Code
- Money is always `Decimal`, never `float`. Round to cents with `ROUND_HALF_UP`.
- For invalid input, raise `shop.errors.AppError` with an UPPER_SNAKE error code.
  Never raise `ValueError` and never return `None` for an error.
- Every public function has a docstring with an `Example:` line.

## Tests
- Add tests for every new function in `tests/test_<module>.py` (unittest).
- Before you finish, run: `python -m unittest discover -s tests -v`

## Housekeeping
- Add one line describing the change to `CHANGELOG.md` under `## Unreleased`.
- Do not add dependencies.
