# AGENTS.md: Bookshop team rules

## Security
- Limits and timeouts (attempt counts, lock minutes) go in auth/config.py, never hard-coded.
- Record every security event with audit_log() from auth/audit.py (for example LOGIN_LOCKED).
- Never put a password, or whether an email exists, in an error message or log.

## Every change
- Add one line to CHANGELOG.md under ## Unreleased.
- Before finishing, run the tests: python -m unittest discover -s tests -v
