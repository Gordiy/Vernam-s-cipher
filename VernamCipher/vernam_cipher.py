from random import randint
from BBS import BBS


class VernamCipher:
    def __init__(self):
        self.encryption_arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    def get_key(self, length: int) -> str:
        key = ""

        for _ in range(length):
            num = 27
            while (num > 26):
                upperbound = 26
                q = randint(0, upperbound)
                bbs = BBS(11, 19)
                num = bbs.get_x_n(q)
            key += self.encryption_arr[num]

        return key
    
    def encrypt(self, plain_text: str, key_bytes: bytearray) -> str:
        plain_text_bytes = bytearray(plain_text, 'utf8')
        encrypted_text = bytearray()
        for i in range(len(plain_text)):
            xor = key_bytes[i] ^ plain_text_bytes[i]
            encrypted_text.append(xor)

        return encrypted_text.decode(encoding='utf8')

    def decrypt(self, cipher_text: str, key_bytes: bytearray) -> str:
        cipher_text_bytes = bytearray(cipher_text, 'utf8')
        decrypte_text = bytearray()
        
        for i in range(len(cipher_text_bytes)):
            xor = key_bytes[i] ^ cipher_text_bytes[i]
            decrypte_text.append(xor)

        return decrypte_text.decode('utf8').upper()
