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

    def test_InValidIPv4Mask(self):
        self.assertFalse(network_fun.IsIPv4Mask("1.1.1"))
        self.assertFalse(network_fun.IsIPv4Mask("255.255.254.255"))
        self.assertFalse(network_fun.IsIPv4Mask("255.255.255.253"))
        self.assertFalse(network_fun.IsIPv4Mask("0.255.255.255"))
        self.assertFalse(network_fun.IsIPv4Mask("128.255.255.255"))
        self.assertFalse(network_fun.IsIPv4Mask("255.255.240.240"))

    def test_ValidIPv4Mask(self):
        self.assertTrue(network_fun.IsIPv4Mask("255.255.255.255"))
        self.assertTrue(network_fun.IsIPv4Mask("255.255.255.254"))
        self.assertTrue(network_fun.IsIPv4Mask("255.255.255.252"))
        self.assertTrue(network_fun.IsIPv4Mask("255.255.255.248"))
        self.assertTrue(network_fun.IsIPv4Mask("255.255.255.240"))
        self.assertTrue(network_fun.IsIPv4Mask("255.255.255.224"))
        self.assertTrue(network_fun.IsIPv4Mask("255.255.255.192"))
        self.assertTrue(network_fun.IsIPv4Mask("255.255.255.128"))
        self.assertTrue(network_fun.IsIPv4Mask("255.255.255.0"))
        self.assertTrue(network_fun.IsIPv4Mask("255.255.254.0"))
        self.assertTrue(network_fun.IsIPv4Mask("255.255.252.0"))
        self.assertTrue(network_fun.IsIPv4Mask("255.255.248.0"))
        self.assertTrue(network_fun.IsIPv4Mask("255.255.240.0"))
        self.assertTrue(network_fun.IsIPv4Mask("255.255.224.0"))
        self.assertTrue(network_fun.IsIPv4Mask("255.255.192.0"))
        self.assertTrue(network_fun.IsIPv4Mask("255.255.128.0"))
        self.assertTrue(network_fun.IsIPv4Mask("255.255.0.0"))
        self.assertTrue(network_fun.IsIPv4Mask("255.254.0.0"))
        self.assertTrue(network_fun.IsIPv4Mask("255.252.0.0"))
        self.assertTrue(network_fun.IsIPv4Mask("255.248.0.0"))
        self.assertTrue(network_fun.IsIPv4Mask("255.240.0.0"))
        self.assertTrue(network_fun.IsIPv4Mask("255.224.0.0"))
        self.assertTrue(network_fun.IsIPv4Mask("255.192.0.0"))
        self.assertTrue(network_fun.IsIPv4Mask("255.128.0.0"))
        self.assertTrue(network_fun.IsIPv4Mask("255.0.0.0"))
        self.assertTrue(network_fun.IsIPv4Mask("254.0.0.0"))
        self.assertTrue(network_fun.IsIPv4Mask("252.0.0.0"))
        self.assertTrue(network_fun.IsIPv4Mask("248.0.0.0"))
        self.assertTrue(network_fun.IsIPv4Mask("240.0.0.0"))
        self.assertTrue(network_fun.IsIPv4Mask("224.0.0.0"))
        self.assertTrue(network_fun.IsIPv4Mask("192.0.0.0"))
        self.assertTrue(network_fun.IsIPv4Mask("128.0.0.0"))
        self.assertTrue(network_fun.IsIPv4Mask("0.0.0.0"))

if __name__ == '__main__':
    unittest.main()
