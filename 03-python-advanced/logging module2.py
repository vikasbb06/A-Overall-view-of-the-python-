import logging
import logging.config
from logging.handlers import RotatingFileHandler,TimedRotatingFileHandler
import time

logging.config.fileConfig('logging.config')
logger=logging.getLogger('simpleExample')
logger.debug('This is a debug message')
try:
    a=[1,2,3]
    al=a[4]
except IndexError as e:
    logging.error(e,exc_info=True) 
loggers=logging.getLogger(__name__)
handler=RotatingFileHandler('app.log',maxBytes=5000,backupCount=5)
time_handler=TimedRotatingFileHandler('timed_app.log',when='s',interval=5,backupCount=3)
loggers.addHandler(handler)
loggers.addHandler(time_handler)
for _ in range(10000):
    loggers.info('Hello! World')
for _ in range(6):
    loggers.info('Hello! World')
    time.sleep(5)



