import logging
# DEBUG
# INFO
# WARNING
# Error
# CRITICAL
# logging.basicConfig(level= logging.DEBUG, filename="logs.log", filemode="w" )
# logging.debug("debug logs")
# logging.info("info logs")
# logging.warning("warning logs")
# logging.error("error logs")
# logging.critical("critical logs")

logging.basicConfig(level= logging.DEBUG, filename="logs.log", filemode="w",format="We have next loging message:%(asctime)s : %(levelname)s - %(message)s")
logging.debug("debug logs")
logging.info("info logs")
logging.warning("warning logs")
logging.error("error logs")
logging.critical("critical logs")
