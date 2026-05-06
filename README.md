# FastAPI Breaking Change Detection

Example project showing how to detect breaking API changes as part of CI/CD for FastAPI applications.

The CI pipeline uses [oasdiff](https://github.com/Tufin/oasdiff) to compare the OpenAPI schema from the PR branch against the main branch. If a breaking change is detected (e.g., removing an endpoint, renaming a field, changing a required parameter), the pipeline fails.

## How It Works

1. A small script (`scripts/export_openapi.py`) exports the OpenAPI spec from the FastAPI app to a JSON file
2. The CI workflow generates specs from both the PR branch and the main branch
3. `oasdiff breaking old.json new.json --fail-on ERR` compares them and fails on breaking changes

## Skipping the Check

If a breaking change is intentional, include `[breaking-change]` in the PR title to skip the check.

## Project Structure

```
app/
  main.py          # FastAPI app with CRUD endpoints
  schemas.py       # Pydantic models (API contract)
scripts/
  export_openapi.py  # Exports OpenAPI spec to JSON
tests/
  test_items.py    # API tests
.github/
  workflows/
    ci.yml         # CI pipeline with breaking change detection
```

## Getting Started

```bash
uv sync
uv run uvicorn app.main:app --reload
```

## Running Tests

```bash
uv run pytest -v
```

## Exporting the OpenAPI Spec

```bash
uv run python scripts/export_openapi.py openapi.json
```
