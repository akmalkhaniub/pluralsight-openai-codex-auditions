# REPOSITORY AGENT GOVERNANCE RULES
# This file governs all code generation, refactoring, and file creation by OpenAI Codex.

## 1. Architectural Boundaries
* All business logic must reside within `src/services/`.
* Controllers/routes must not contain direct network or persistence logic; they must delegate to service classes.

## 2. Dependency Whitelist
* **HTTP Client:** MUST use asynchronous `httpx.AsyncClient`. 
* **Forbidden Packages:** Strictly DO NOT use `requests`, `urllib3`, or `aiohttp`.
* **Logging:** Use Python's standard `logging.getLogger(__name__)`. DO NOT use raw `print()` statements in production code.

## 3. Error Handling Standards
* Never use bare `except:` blocks or swallow exceptions with `pass`.
* When an external webhook or network call fails, raise `NotificationDeliveryError` (subclass of `AppError` located in `src.errors.app_error`).
* Always include the original error message and HTTP status code in the exception context.

## 4. Test Generation Mandate
* Whenever a new service is created in `src/services/<service_name>.py`, Codex MUST automatically create a companion unit test in `tests/services/test_<service_name>.py`.
* Tests must use `pytest` and `pytest-asyncio` with mocked network calls (no real outbound HTTP traffic during test runs).
