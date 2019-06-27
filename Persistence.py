import numpy


class Persistence:

    def __init__(self, number):
        # setting self number to input number
        self.number = number

    def prod(self):
        # initiates two variables, integers, and prod. Should change to defined vars
        integers = []
        # for loop turns the number > str > array
        for i in str(self.number):
            integers.extend([int(i)])
        # returns the product as an integer of the array
        return numpy.prod(integers)

    def persistence(self):
        # Sets variables persistence as int, and num as self.number
        persistence = 0
        num = self.number
        # While loop to continue to take product of int
        while len(str(num)) > 1:
            persistence = persistence + 1
            num = Persistence(num).prod()
        return persistence
