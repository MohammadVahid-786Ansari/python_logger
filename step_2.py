import logging

logging.basicConfig(filename='file.log',
                    level=logging.INFO,
                    datefmt = '%m/%d/%Y %I:%M:%S %p',
                    format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')
# logging.basicConfig(filename='file.log',
#                     level=logging.DEBUG,
#                     datefmt="%y%d",
#                     format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

logging.debug('Debug message')
logging.info('Info message')
logging.warning('Warning message')
logging.error('Error message')
logging.critical('Critical message')
