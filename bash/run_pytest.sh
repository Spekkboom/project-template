#!bin/bash

# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=my_project

# Run with coverage and show missing lines
uv run pytest --cov=my_project --cov-report=term-missing

# Run specific test file
uv run pytest tests/test_main.py

# Run tests matching a pattern
uv run pytest -k "test_greet"

# Run with verbose output
uv run pytest -v