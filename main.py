from LFSR import LFSR
from BBS import BBS
from VernamCipher import VernamCipher


bbs = BBS(11, 19)
vm = VernamCipher()
plain_text = "hello"
vm_key = vm.get_key_based_on_bbs(13)
cipher_encrypt = vm.encrypt(plain_text, bytearray(vm_key, 'utf8'))
print("Encryption:", cipher_encrypt)
cipher_decrypt = vm.decrypt(cipher_encrypt, bytearray(vm_key, 'utf8'))
print("Decryption:", cipher_decrypt)

lfsr_key = LFSR.get_key()
cipher_encrypt = vm.encrypt(plain_text, bytearray(lfsr_key))
print("Encryption:", cipher_encrypt)
cipher_decrypt = vm.decrypt(cipher_encrypt, bytearray(lfsr_key))
print("Decryption:", cipher_decrypt)
