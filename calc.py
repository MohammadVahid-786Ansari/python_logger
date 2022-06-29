import logging
import car_class

# logging.basicConfig(filename = 'calc.log', level = logging.DEBUG ,
#                     format = '%(asctime)s:%(name)s:%(message)s',
#                     )

logger = logging.getLogger('calc')
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler = logging.FileHandler('calc.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


def add(x, y):
    """Add Function"""
    return x + y
def subtract(x, y):
    """Subtract Function"""
    return x - y
def multiply(x, y):
    """Multiply Function"""
    return x * y
def divide(x, y):
    """Divide Function"""
    return x / y

num_1 = 10
num_2 = 2

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))









