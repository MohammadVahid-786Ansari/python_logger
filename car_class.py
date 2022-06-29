import logging

# logger = logging.getLogger('car')
# logger.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
#
# file_handler = logging.FileHandler('car_class.log')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)


logger = logging.getLogger("car")
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('car_class.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)






# logging.basicConfig(filename= "car_class.log" ,level = logging.INFO, format='%(asctime)s:%(name)s:%(levelname)s:%(message)s')

class car:
    def __init__(self,name,speed,milage):
        self.name = name
        self.speed = speed
        self.milage = milage
        logger.info(f"{self.name} has been created speed is {self.speed} and speed is {self.milage}")
    # print('class created successfully')

obj1 = car('bmw',100,50)
obj2 = car('ciaz',20,30)
print(obj1.speed)




