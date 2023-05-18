#!/usr/bin/env bash

set -e
set -x

mypy src
ruff src
black src --check
isort src --check-only
