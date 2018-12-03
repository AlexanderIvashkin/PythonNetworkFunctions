def IsIPv4Address(ipAdd):
    """Validate an IPv4 address"""
    octets = ipAdd.split(".")
    if len(octets) != 4:
        return False
    return True

if IsIPv4Address(input("Gimme you address! ")):
    print ("TRUEЪ")
else:
    print ("NOT TRUEЪ")

