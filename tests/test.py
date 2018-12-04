import unittest
import network_fun

class UnitTestsCase(unittest.TestCase):

    def test_ValidIPv4Address(self):
        self.assertTrue(network_fun.IsIPv4Address("1.1.1.1"))
        self.assertTrue(network_fun.IsIPv4Address("1.1.1.2"))
        self.assertTrue(network_fun.IsIPv4Address("255.1.1.2"))
        self.assertTrue(network_fun.IsIPv4Address("255.1.1.255"))
        self.assertTrue(network_fun.IsIPv4Address("255.255.255.255"))
        self.assertTrue(network_fun.IsIPv4Address("0.0.0.0"))

    def test_InValidIPv4Address(self):
        self.assertFalse(network_fun.IsIPv4Address("1.1.1"))
        self.assertFalse(network_fun.IsIPv4Address("1.1"))
        self.assertFalse(network_fun.IsIPv4Address("1.1.1."))
        self.assertFalse(network_fun.IsIPv4Address("25.1.1.256"))
        self.assertFalse(network_fun.IsIPv4Address("FF.1.1.256"))
        self.assertFalse(network_fun.IsIPv4Address("1.1.-1.23"))
        self.assertFalse(network_fun.IsIPv4Address("1.1.a1.23"))

#     def test_InValidIPv4Mask(self):
#         self.assertFalse(network_fun.IsIPv4Mask("1.1.1"))

    def test_ValidSubnetOctet(self):
        self.assertTrue(network_fun.IsMaskOctet("0"))

if __name__ == '__main__':
    unittest.main()
