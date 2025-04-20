import unittest
from rsa import RSA

class TestRSA(unittest.TestCase):

    def setUp(self):
        self.p = 61
        self.q = 53
        self.rsa = RSA(p=self.p, q=self.q)

    def test_n(self):
        self.assertEqual(self.rsa.n, 61 * 53)

    def test_phi(self):
        expected_phi = (self.p - 1) * (self.q - 1)
        self.assertEqual(self.rsa.phi, expected_phi)

    def test_encryption_decryption(self):
        plaintext = 42
        ciphertext = self.rsa.encrypt(plaintext)
        decrypted_plaintext = self.rsa.decrypt(ciphertext)
        self.assertEqual(decrypted_plaintext, plaintext)

if __name__ == '__main__':
    unittest.main()