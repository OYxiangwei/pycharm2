import logging
import time
#logging.debug("this debug")

#logging.log(logging.DEBUG,"this debug")

#log_format = "%(asctime)s --%(created)f--%(levelname)s--%(message)s"
#logging.basicConfig(filename="错误日志.log",level=logging.DEBUG,format=log_format)
#print()


import logging
import logging.handlers
import datetime
logger = logging.getLogger('myloger')
logger.setLevel(logging.DEBUG)

rf_handler=logging.handlers.TimedRotatingFileHandler('all.log',when="midnight",backupCount=7,interval=1)
rf_handler.setFormatter(logging.Formatter("%(asctime)s --%(created)f--%(levelname)s--%(message)s"))

f_handler=logging.FileHandler("error.log")
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s --%(created)f--%(levelname)s--%(message)s"))

logger.addHandler(rf_handler)
logger.addHandler(f_handler)

logger.debug("debug")
logger.error('error')

