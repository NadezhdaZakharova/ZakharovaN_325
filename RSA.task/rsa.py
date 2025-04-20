import random
from sympy import isprime

class RSA:
    def __init__(self, p=None, q=None):
        if p is None or q is None:
            raise ValueError("Please, provide p and q")
        if not (isprime(p) and isprime(q)):
            raise ValueError("Use only prime numbers")
        self.p = p
        self.q = q
        self.n = p * q
        self.phi = (p - 1) * (q - 1)
        self.e = self._find_e()
        self.d = self._mod_inverse(self.e, self.phi)

    def _find_e(self):
        e = 3
        while e < self.phi:
            if self._gcd(e, self.phi) == 1:
                return e
            e += 2
        raise ValueError("Could not find a suitable e.")

    def _gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def _mod_inverse(self, a, m):
        m0, x0, x1 = m, 0, 1
        if m == 1:
            return 0
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += m0
        return x1

    def encrypt(self, plaintext):
        return pow(plaintext, self.e, self.n)

    def decrypt(self, ciphertext):
        return pow(ciphertext, self.d, self.n)