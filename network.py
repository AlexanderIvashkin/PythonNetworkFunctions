def IsIPv4Address(ipAdd):
    """Validate an IPv4 address"""
    octets = ipAdd.split(".")
    print (octets)

IsIPv4Address(input("Gimme you address! "))

