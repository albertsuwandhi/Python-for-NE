#/usr/bin/env python3
#DEBUG, INFO, WARNING, ERROR, CRITICAL
import logging
# basicConfig() to configure the root logger works only if the root logger has not been configured before.
# This function can only be called once.
# The default setting in basicConfig() is to set the logger to write to the console
# by default only log Warning and Above, the line below change the level

# logging.basicConfig(level=logging.DEBUG)

# Set Logging to File
logging.basicConfig(filename='./app.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logging.debug("Debug Message")
logging.info("Info Message")
logging.warning("Warning Message")
logging.error("Error Message")
logging.critical("Critical Message")



