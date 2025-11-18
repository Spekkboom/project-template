#!bin/bash

pip install uv

cd ..

uv init --no-readme
uv add --dev mkdocs mkdocs-material
uv run mkdocs new ../.

uv sync
