# Lambda Layer Manager

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
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
      "name": "<name_of_the_layer>",
      "requirements": "<path_to_requirements_file>",
      "config": {
        "description": "<description>",
        "compatible_runtimes": ["<python3.10>"],
        "compatible_architectures": ["<x86_64>"]
      }
    }
  ]
}
```

An example configuration can be found in the `./example` directory.

## Quickstart

Run the *Lambda Layer Manager* (*llm*) with the following command:
```bash
llm <path/to/config_file>
```

## Contribution

Install the dependencies:
```bash
poetry install
```

Enable the *pre-commit* hooks:
```bash
pre-commit install
```

## License

This project is licensed under the MIT license.
