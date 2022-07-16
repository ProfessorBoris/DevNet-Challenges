# Check if an inputted IPv4 address is valid
# Author: B.Lorkovic 15/07/2022
# 

def enter_IP_address():
    print("Enter an IPv4 address (Type x to end): ")
    IP_Address_str = input()
    return IP_Address_str

def validate_IP_Address(IP_address):
    parts = IP_address.split(".")

    if len(parts) != 4:
        print("{} is not a valid IPv4 address".format(IP_address))
        print("It's not the right length and/or format")
        return False
    
    for part in parts:
        try:
            x = isinstance(int(part), int)
        except:
            print("{} is not a valid IPv4 address".format(IP_address))
            print("you used non-integer values")
            return False

        if int(part) < 0 or int(part) > 255:
            print("{} is not a valid IPv4 address".format(IP_address))
            print("The value {} is out of the allowable range of values".format(part))
            return False

    print("{} is a valid IPv4 address".format(IP_address))
    return True
  
        
while True:
    IP_address =  enter_IP_address()
    if IP_address == "x":
        break
    IP_address_in_parts = validate_IP_Address(IP_address)

