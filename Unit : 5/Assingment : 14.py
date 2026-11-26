#Assingment : 14


import logging

#set logging details
logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s: %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log", mode="w")
    ]
)

print("Logging messages are shown below.", flush=True)

#display different logging messages
logging.debug("Checking program details.")
logging.info("Program started successfully.")
logging.warning("Please check the entered data.")
logging.error("An error occurred in the program.")
logging.critical("Program stopped due to a serious error.")

#Output
'''Logging messages are shown below.
DEBUG: Checking program details.
INFO: Program started successfully.
WARNING: Please check the entered data.
ERROR: An error occurred in the program.
CRITICAL: Program stopped due to a serious error.'''
