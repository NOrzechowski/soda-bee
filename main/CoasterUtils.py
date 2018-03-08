import numpy as np


class CoasterUtils:

    def __init__(self):
        self.attribute_names = ['is-not-divisible', 'divisible-by-3', 'divisible-by-5', 'divisible-by-7', 'divisible-by-3&5',
                       'divisible-by-3-7', 'divisible-by-5&7', 'divisible-by-3&5&7', 'class']


    def encode(self, i):
        if i % 3 == 0:
            if i % 5 == 0:
                if i % 7 == 0:
                    return np.array([0, 0, 0, 0, 0, 0, 0, 1, "floofbangwham"])
                return np.array([0, 0, 0, 0, 1, 0, 0, 0, "floofbang"])
            elif i % 7 == 0:
                return np.array([0, 0, 0, 0, 0, 1, 0, 0, "floofwham"])
            return np.array([0, 1, 0, 0, 0, 0, 0, 0, "floof"])
        elif i % 5 == 0:
            if i % 7 == 0:
                return np.array([0, 0, 0, 0, 0, 0, 1, 0, "bangwham"])
            return np.array([0, 0, 1, 0, 0, 0, 0, 0, "bang"])
        elif i % 7 == 0:
            return np.array([0, 0, 0, 1, 0, 0, 0, 0, "wham"])
        else:
            return np.array([1, 0, 0, 0, 0, 0, 0, 0, "number"])

    def get_val(self, i):
        val = self.encode(i)[8]
        if val == "number":
            return str(i)
        else:
            return val


    def get_attribute_names(self):
        return self.attribute_names