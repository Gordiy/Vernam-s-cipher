"""
Linear feedback shift register. 
"""


class LFSR:
    """
    x^11+x^2+1
    """
    @staticmethod
    def get_key():
        s = []
        register = [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]

        for i in range(3255):
            s.append(register[0] ^ register[2] ^ register[11])
            first_byte = register[0]
            register[0] = register[11] ^ register[10]

            # register[11] = register[10]
            # register[10] = register[9]

            for j in range(len(register)-1, 1, -1):
                register[j] = register[j-1]

            register[1] = first_byte

        return s
