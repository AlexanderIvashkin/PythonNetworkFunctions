# Version: 1.1.0

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

def IsIPv4Mask(ipMask):
    """Validate an IPv4 subnet mask"""

    # Each mask looks like an IPv4 address and must pass the checks
    if not IsIPv4Address(ipMask):
        return False

    ipMaskBinary = ""
    ipMaskBinary = ipMaskBinary.join([bin(int(oct))[2:] for oct in ipMask.split(".")])

    isBitZero = ipMask[0] == "0"
    for bit in ipMask[1:]:
        if bit == "1" and isBitZero:
                return False

        if bit == "0":
            isBitZero = True

    return True
