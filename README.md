
Demo showing how to use loguru to log from this script (main.py) and also from 2 imported modules (module1.py, module2.py)
Output is sent to the terminal and a log file (logurutest.log). The log file is configured using logurutest_config.py towrite to loguru.log, which is rotated at midnight.

Terminal command: 
```bash
uv run main.py
```

Note that The following code module1.py and module2.py can be executed indepentently as scripts and they will continue to append messages to logurutest.log.

Terminal commands:
```
uv run module1.py
uv run module2.py
```
