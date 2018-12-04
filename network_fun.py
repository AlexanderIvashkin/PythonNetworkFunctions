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


# if IsIPv4Address(input("Gimme you address! ")):
#     print ("TRUEЪ")
# else:
#     print ("NOT TRUEЪ")
