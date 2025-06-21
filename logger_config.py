from loguru import logger
import sys

def initialize_logger():
    """ 
    Initializes loguru.logger to output to the stderr (the terminal) and also to a log file (logurutest).
    The log file will be rotated at midnight.
    """
    log_level = "DEBUG"
    log_format = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS zz}</green> | <level>{level: <8}</level> | <yellow>Line {line: >4} ({file}):</yellow> <b>{message}</b>"
    logger.remove()
    logger.add(sys.stderr, level=log_level, format=log_format, colorize=True, backtrace=True, diagnose=True)
    logger.add("logurutest.log", level=log_level, format=log_format, colorize=False, backtrace=True, diagnose=True, rotation='00:00')
