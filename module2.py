from loguru import logger

def logentry():
    logger.info('hi from module2.py')

# The following code is run only when this module is executed as a script
# For example, by issuing the following command in a terminal:
#   uv run module2.py
if __name__ == "__main__":
    import logger_config
    logger_config.initialize_logger()
    logentry()
