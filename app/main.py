
from loguru import logger

#
# Logging -> cf. https://github.com/Delgan/loguru
#
logger.add("logs/app.log")

#
# Entry points
#
def start():
    """Launched with `poetry run start` at project root level"""
    logger.debug("Hi there!")
    logger.warning("Hi there!")


if __name__ == "__main__":
    """Python module entry point. Is run via `python -m app.main` e.g. on Docker container start (cf. Dockerfile)"""
    start()
