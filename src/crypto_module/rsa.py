import random
import math

class Cryptography:
    @staticmethod
    def is_prime(n):
        if (n < 2):
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def generate_prime(bits):
        while True:
            n = random.getrandbits(bits)
            if Cryptography.is_prime(n):
                return n
        
    @staticmethod
    def mod_inverse(a, m):
        for i in range(1, m):
            if (a*i) % m == 1:
                return i
        return None
    
    @staticmethod
    def left_rotate(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff
    
class RSA:
    @staticmethod
    def generate_keys(bits=1024):
        p = Cryptography.generate_prime(bits // 2)
        q = Cryptography.generate_prime(bits // 2)
        n = p * q
        phi = (p - 1) * (q - 1)
        
        for i in range(2, phi):
            if math.gcd(i, phi) == 1:
                e = i
                break
        
        d = Cryptography.mod_inverse(e, phi)
        
        return ((n, e), (n, d))
    
    @staticmethod
    def encrypt(message, public_key):
        n, e = public_key
        return [pow(ord(char), e, n) for char in message]
    
    @staticmethod
    def decrypt(encrypted_message, private_key):
        n, d = private_key
        return ''.join([chr(pow(char, d, n)) for char in encrypted_message])
    