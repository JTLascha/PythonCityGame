""" This is the skeleton for the Person class - lots still to do on this """
from enum import Enum

from . import squares

class Job(Enum):
    UNEMPLOYED = 0
    FACTORY_WORKER = 1
    CONSTRUCTION_WORKER = 2
    FARMER = 3

class Person:
    # home_location and job_location should be the index 
    # of the square where they live/work
    def __init__(self, age, job, job_location, home_location, index):
        self.age = age
        self.job = job
        self.home_location = home_location
        self.job_location = job_location
        self.index = index

    # This will calculate the persons happiness level
    # with an as yet to be determined algorithm taking
    # into account their job, living location etc
    def happiness(self):
        pass
