# Lambda Layer

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat-square&labelColor=ef8336)](https://pycqa.github.io/isort/)

## Overview

Automatically build and deploy AWS Lambda layer.

**Config:**
```json
{
    "layers": [
        {
            "requirements": <path_to_requirements_file>,
            "config": {
                "name": <name_of_the_layer>,
                "description": <description>,
                "compatible_runtimes": [],
                "compatible_architectures": []
            }
        }
    ]
}
```
