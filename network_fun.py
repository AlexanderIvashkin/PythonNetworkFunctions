# Version: 1.1.0

import math

def IsNumber(num):
    try:
        float(num)
    except ValueError:
        return False
    return True

def IsInteger(num):
    try:
        if int(num) == float(num):
            return True
        else:
            return False
    except ValueError:
        return False
    return True

def IsIPv4Address(ipAdd):
    """Validate an IPv4 address"""
    octets = ipAdd.split(".")
    if len(octets) != 4:
        return False
    for octet in octets:
        if not IsInteger(octet):
            return False
        if int(octet) > 255 or int(octet) < 0:
            return False

    return True

# TODO unit tests for this func (all the possible values)
def IsMaskOctet(octet):
    if not IsInteger(octet):
        return False
    isBitZero = bin(octet)[2] == "0"
    for bit in bin(octet)[3:]:
        if bit == "1" and isBitZero:
            return False

    return True

def IsIPv4Mask(ipMask):
    """Validate an IPv4 subnet mask"""

    # Each mask looks like an IPv4 address and must pass the checks
    if not IsIPv4Address(ipMask):
        return False

    for octet in octets:
        if not IsMaskOctet(octet):
            return False

    return True
