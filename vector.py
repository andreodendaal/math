import numpy as np


class Vector(object):
    def __init__(self, coordinate1, coordinate2):
        try:
            if not coordinate1 and not coordinate2:
                raise ValueError
            self.coordinate_1 = np.array(coordinate1)
            self.coordinate_2 = np.array(coordinate2)
            self.dimension = len(coordinate1) + len(coordinate2)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinate_1 + self.coordinate_2)

    def add_vectors(self):
        vector_sum = self.coordinate_1 + self.coordinate_2
        return str(vector_sum)

    def multiply_vectors(self, mult):
        vector_mult = self.coordinate_1 * mult
        return str(vector_mult)

    def subtract_vectors(self):
        vector_sub = self.coordinate_1 - self.coordinate_2
        return str(vector_sub)
