#!/usr/bin/env bash

set -e
set -x

ruff src
black src --check
isort src --check-only
