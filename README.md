# Python + Poetry project template

## What's inside

A ready to go project structure with

- Python, version 3.12 or above.
- [Poetry package/dependency manager](https://python-poetry.org/).
- [Multi-stage `Dockerfile`](./Dockerfile) for containerizing this poetry project.
- [Configured `pre-commit`](https://pre-commit.com/) checks.
- [Configured logging](./app/app_logging/setup.py): handlers (non-blocking queue handler, file-based handler and stderr) and formatters (simple and JSON).
- Business logic is intended to go into the package called `/app`.


## Getting started

### Minimum steps for running the application
Depending on your setup, some steps might not be necessary

- [ ] Set python version to be used for the project with `poetry env use [path/to/python/executable]`
    - Alternatively set the python version via `pyenv`. Check [here](https://www.youtube.com/watch?v=3my06DUnApM) and [here](https://medium.com/@adocquin/mastering-python-virtual-environments-with-pyenv-and-pyenv-virtualenv-c4e017c0b173) for infos about `pyenv`.
    - NOTE: python version must be 3.12 or above
- [ ] Install virtual environment and project dependencies with `poetry install`
- [ ] Start the application through a pre-defined poetry script with `poetry run start`.

### Additional steps to get ready for development
Depending on your setup, some steps might not be necessary
- [ ] Initialize git repository with `git init`
- [ ] Add dependencies with `poetry add [depencency-name]`
- [ ] Add dependencies to a specified group (e.g. dev dependencies) with `poetry add [depencency-name] --group [group-name]`
- [ ] Configure pre-commit hooks with `poetry run pre-commit install`
- [ ] Run pre-commit hooks once on all files with `poetry run pre-commit run --all-files`
- [ ] Run tests with `poetry run pytest`
