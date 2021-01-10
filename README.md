[![Build Status](https://github.com/ConorSheehan1/cookiecutter-fire-cli/workflows/ci/badge.svg)](https://github.com/ConorSheehan1/cookiecutter-fire-cli/actions/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This repo contains a [cookiecutter](https://github.com/audreyr/cookiecutter) template for creating a new python package with a  [fire](https://github.com/google/python-fire) command line interface.

# Usage
To create a new project using this cookiecutter template:

```bash
pip install cookiecutter
cookiecutter gh:ConorSheehan1/cookiecutter-fire-cli
```

For full cookiecutter instructions see https://github.com/audreyr/cookiecutter#features

# Configuration provided
1. testing
    1. pytest
    1. github actions
1. linting
    1. black
    1. isort
    1. mypy
1. dependency management / packaging
    1. poetry
1. version management
    1. bump2version
1. license
    1. MIT

### Local/Dev install
```bash
poetry install
poetry run cookiecutter .
# poetry run cookiecutter . --overwrite-if-exists --no-input
```
