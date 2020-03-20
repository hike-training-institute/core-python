import logging
from logging.handlers import RotatingFileHandler
import os
app_folder = os.path.dirname(os.path.dirname(__file__))
script_mode_folder = os.path.join(app_folder, 'script_mode')
food_billing_log_file_name = 'food_billing_app.log'
food_billing_log_file_path = os.path.join(script_mode_folder, food_billing_log_file_name)



food_bill_logger = logging.getLogger('food_billing_logger')
file_handler = RotatingFileHandler(food_billing_log_file_path, mode='a+', maxBytes=1024 * 1024 * 100, backupCount=20)
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - [%(filename)s:%(lineno)s - %(funcName)20s() ] - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
food_bill_logger.addHandler(file_handler)