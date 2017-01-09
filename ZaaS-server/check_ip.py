import ipaddress
import netifaces

def check_ip(my_net):
    for interface in netifaces.interfaces():
        if 2 in netifaces.ifaddresses(interface):
            if ipaddress.ip_address(netifaces.ifaddresses(interface)[2][0]['addr']) in ipaddress.ip_network(my_net):
                return True
            else:
                continue
    return False
