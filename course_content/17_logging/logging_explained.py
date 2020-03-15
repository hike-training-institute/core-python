import logging
from logging.handlers import RotatingFileHandler

server_log = logging.getLogger('server')
app_log = logging.getLogger('app')
db_log = logging.getLogger('db')


file_handler = RotatingFileHandler('server.log', maxBytes=1024 * 1024 * 100, backupCount=20)
file_handler.setLevel(logging.CRITICAL)
formatter = logging.Formatter("%(asctime)s - [%(filename)s:%(lineno)s - %(funcName)20s() ] - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
server_log.addHandler(file_handler)
server_log.warning("server critical")


file_handler = RotatingFileHandler('app.log', maxBytes=1024 * 1024 * 100, backupCount=20)
file_handler.setLevel(logging.CRITICAL)
formatter = logging.Formatter("%(asctime)s - [%(filename)s:%(lineno)s - %(funcName)20s() ] - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
app_log.addHandler(file_handler)
app_log.warning("app critical")




# from logging.handlers import RotatingFileHandler
# logger = logging.getLogger('app')
# file_handler = RotatingFileHandler('app.log', maxBytes=1024 * 1024 * 100, backupCount=20)
# formatter = logging.Formatter("%(asctime)s - [%(filename)s:%(lineno)s - %(funcName)20s() ] - %(levelname)s - %(message)s")
# file_handler.setFormatter(formatter)
# file_handler.setLevel(logging.INFO)
# logger.addHandler(file_handler)
#
# logger.debug("logging to file...")
# logger.info("logging to file...")
# logger.warning("logging to file...")
# logger.error("logging to file...")
# logger.critical("logging to file...")
