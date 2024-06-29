import math
import hashlib

class SHA1:
    def __init__(self):
        self.h = [
            0x67452301,
            0xEFCDAB89,
            0x98BADCFE,
            0x10325476,
            0xC3D2E1F0
        ]
    
    def sha1(self, message):
        if isinstance(message, str):
            message = message.encode()

        # Pre-processing
        ml = len(message) * 8
        message += b'\x80'
        while (len(message) % 64) != 56:
            message += b'\x00'
        message += ml.to_bytes(8, 'big')
        print(message)

        # Process the message in 512-bit chunks
        for i in range(0, len(message), 64):
            self._process_chunk(message[i:i+64])

        # Produce the final hash value
        return ''.join(f'{h:08x}' for h in self.h)
    
    def _process_chunk(self, chunk):
        w = [0] * 80
        
        # Break chunk into sixteen 4-byte big-endian words
        for i in range(16):
            w[i] = int.from_bytes(chunk[i*4:i*4+4], 'big')
        
        # Extend the sixteen 4-byte words into eighty 4-byte words
        for i in range(16, 80):
            w[i] = self._left_rotate(w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16], 1)
        
        # Initialize hash value for this chunk
        a, b, c, d, e = self.h

        # Main loop
        for i in range(80):
            if i < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif i < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif i < 60:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            else:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = (self._left_rotate(a, 5) + f + e + k + w[i]) & 0xFFFFFFFF
            e = d
            d = c
            c = self._left_rotate(b, 30)
            b = a
            a = temp

        # Add this chunk's hash to result so far
        self.h = [(x + y) & 0xFFFFFFFF for x, y in zip(self.h, [a, b, c, d, e])]

    @staticmethod
    def _left_rotate(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xFFFFFFFF
    
class SHA256:
    def __init__(self):
        self.h = [
            0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
            0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19
        ]
        
        self.k = [
            0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
            0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
            0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
            0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
            0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
            0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
            0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
            0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2
        ]

    def sha256(self, message):
        if isinstance(message, str):
            message = message.encode()
        
        message = self._pad_message(message)
        
        for chunk_start in range(0, len(message), 64):
            self._process_chunk(message[chunk_start:chunk_start + 64])
        
        return ''.join(f'{x:08x}' for x in self.h)

    def _pad_message(self, message):
        message_len = len(message) * 8
        message += b'\x80'
        while (len(message) + 8) % 64 != 0:
            message += b'\x00'
        message += message_len.to_bytes(8, byteorder='big')
        return message

    def _process_chunk(self, chunk):
        w = [int.from_bytes(chunk[i:i+4], byteorder='big') for i in range(0, 64, 4)]
        
        for i in range(16, 64):
            s0 = self._right_rotate(w[i-15], 7) ^ self._right_rotate(w[i-15], 18) ^ (w[i-15] >> 3)
            s1 = self._right_rotate(w[i-2], 17) ^ self._right_rotate(w[i-2], 19) ^ (w[i-2] >> 10)
            w.append((w[i-16] + s0 + w[i-7] + s1) & 0xFFFFFFFF)
        
        a, b, c, d, e, f, g, h = self.h
        
        for i in range(64):
            S1 = self._right_rotate(e, 6) ^ self._right_rotate(e, 11) ^ self._right_rotate(e, 25)
            ch = (e & f) ^ ((~e) & g)
            temp1 = (h + S1 + ch + self.k[i] + w[i]) & 0xFFFFFFFF
            S0 = self._right_rotate(a, 2) ^ self._right_rotate(a, 13) ^ self._right_rotate(a, 22)
            maj = (a & b) ^ (a & c) ^ (b & c)
            temp2 = (S0 + maj) & 0xFFFFFFFF
            
            h = g
            g = f
            f = e
            e = (d + temp1) & 0xFFFFFFFF
            d = c
            c = b
            b = a
            a = (temp1 + temp2) & 0xFFFFFFFF
        
        self.h = [(x + y) & 0xFFFFFFFF for x, y in zip(self.h, [a, b, c, d, e, f, g, h])]
        
    @staticmethod
    def _right_rotate(n, d):
        return (n >> d) | (n << (32 - d)) & 0xFFFFFFFF
    
if __name__ == "__main__":
    msg = "abc"
    sha256 = SHA256()
    result = sha256.sha256(msg)
    sha256_lib = hashlib.sha256()
    sha256_lib.update(msg.encode())
    print(result)
    print(sha256_lib.hexdigest())
    