---
name: api-docgen
description: Generates standardized, enterprise API documentation with parameter tables and error status code matrices.
---

# API Documentation Generator Skill

When triggered with a target route or controller file, follow these strict instructions:

## Instructions
1. **Analyze Endpoint:** Parse the HTTP method, URL path, request body, headers, and query parameters.
2. **Document Parameters:** Create a markdown table with columns: `Parameter`, `Type`, `Required`, and `Description`.
3. **Analyze Error Cases:** Inspect all raised HTTPExceptions, validation errors, and third-party call exceptions. Construct an **HTTP Status Code Matrix** documenting:
   - `Status Code` (e.g. 200, 400, 402, 422, 500)
   - `Error Code / Message`
   - `Condition / Cause`
4. **Generate cURL Example:** Provide an exact, copy-pasteable `curl` snippet with dummy authentication headers and sample JSON payload.
5. **Output Target:** Save or preview the output in `docs/api/<endpoint_name>.md`.
