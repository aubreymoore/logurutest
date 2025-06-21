# Demo showing how to use loguru to log from this script (main.py) and also from 2 imported modules (module1.py, module2.py)
# Output is sent to the terminal and a file (logurutest.log) 
#
# Usage:
#   uv run main.py

import logger_config
import module1
import module2
from loguru import logger

logger_config.initialize_logger()
logger.info('hi from main.py')
module1.logentry()
module2.logentry()