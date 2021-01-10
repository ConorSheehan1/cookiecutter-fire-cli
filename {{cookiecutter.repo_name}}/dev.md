### Dev Install
```bash
poetry install

# install osxdocker as symlink to avoid reinstall whenever code changes
# https://github.com/python-poetry/poetry/issues/1135
# workaround using __name__ == '__main__' and fire
poetry run task dev
```

### Test pypi install
```bash
# install from test pypi, allow pull from non-test pypi for fire
pip3 install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple osxdocker
```

### Dev tools
#### Deploy
https://github.com/python-poetry/poetry manages building and deploying.  
You'll need one of the following:
1. `~/.pypirc` set up
2. pass the `--username` and `--password` to publish commands
3. use `POETRY_HTTP_BASIC_PYPI_USERNAME` and `_PASSWORD` environment variables

A github action pushes every git tag to pypi.
A webhook polls the github repo to keep the docs in sync.

```bash
# build dist
poetry build

# publish to test pypi https://github.com/python-poetry/poetry/issues/742#issuecomment-609642943
poetry config repositories.testpypi https://test.pypi.org/legacy/
# ensure latest version is built
poetry publish --build --repository testpypi

# publish to real pypi
poetry publish --build
```

#### Tests
```bash
poetry run task tests
```

#### Linter
```bash
# to autoformat python code using black
poetry run task lint

# to sort imports
poetry run task isort
```

#### Version management
```bash
# pass args e.g. patch, minor, major
poetry run bumpversion --commit --tag patch

# e.g. typical release cycle
poetry run task tests
poetry run task ci_lint
poetry run bumpversion --commit --tag patch
git push
git push --tags

poetry config repositories.testpypi https://test.pypi.org/legacy/
poetry publish --build --repository testpypi
```

Source of truth is .bumpversion.cfg.
See https://github.com/ConorSheehan1/osxdocker/issues/7 and https://github.com/python-poetry/poetry/issues/144#issuecomment-440061951

#### Git hooks
```bash
poetry run task install_hooks
# use --force to overwrite hooks if they already exist
```