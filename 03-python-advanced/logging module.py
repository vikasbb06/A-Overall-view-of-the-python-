import logging
# 5 different log levels:DEBUG,INFO,WARNING,ERROR,CRITICAL ,We have to set basic configuration or only
# level below warning is displayed by default.
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s -%(name)s- %(levelname)s - %(message)s',datefmt='%d/%m/%Y,%I:%M:%S %p')
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")
print("\n---------------------------------------")
logger=logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s- %(message)s')
logger.info("This is an info message from logger")
logger.critical("This is a critical message from logger")
logger.debug("This is a debug message from logger")
#handlers 2:stream,file handlers
stream_handlers=logging.StreamHandler()
file_handlers=logging.FileHandler("filehandling.log")
#level and format
stream_handlers.setLevel(logging.WARNING)
file_handlers.setLevel(logging.ERROR)
stream_format=logging.Formatter('%(asctime)s-%(name)s -%(levelname)s-%(message)s')
file_format=logging.Formatter('%(asctime)s-%(name)s -%(levelname)s-%(message)s')
logger.addHandler(stream_handlers)
logger.addHandler(file_handlers)
logger.warning("This is a warning message")
logger.error("This is an error message")