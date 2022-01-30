"""
Definition Blum Blum Shub (BBS) is used as a pseudo-random number generator.
Realized by: https://intuit.ru/studies/courses/691/547/lecture/12383?page=3
"""
from random import randint
from .utils import next_usable_prime, lcm


class BBS:
    """Pseudo-random numbers."""
    def __init__(self, x, y):
        """
        :param x: is prime number
        :param y: is a prime number
        :param mfactor: is compute by p * q
        """
        self.p = next_usable_prime(x)
        self.q = next_usable_prime(y)
        self.m_factor = self.p * self.q
        self.__x = self.__get_x()
        self.seed = (self.__x**2) % self.m_factor
        self.__xn = self.seed

    def __get_x(self):
        check = False
        x = 0

        while not check:
            upperbound = 26
            x = randint(0, upperbound)
            check = True
            for i in range(2, self.m_factor):
                if x % i == 0 and self.m_factor % i == 0:
                    check = False
        return x

    def get_list_of_bits(self, n: int) -> list:
        """
        Generate list of bits

        :param n: lenght of the number to generate in bits
        :return: random list of bits
        """
        out = []
        for _ in range(n):
            self.__xn = pow(self.__xn, 2, self.m_factor)
            out.append(self.__xn % 2)
        return out

    def convert_from_bits_list_to_int(self, n) -> int:
        """
        Show list of bits as integer type.

        :param n: lenght of the number to generate in bits
        :return: random list of bits as integer type
        """
        return ''.join(self.get_list_of_bits(n))

    def get_x_n(self, n: int) -> int:
        """
        :param n: number of x
        :return: return x in 
        """
        val = pow(2, n, lcm(self.p-1, self.p-1))
        return pow(self.seed, val, self.m_factor) % 2
