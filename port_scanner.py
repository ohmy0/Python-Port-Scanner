import socket 

#Variables
frequent_ports = [445, 22, 23, 25, 11, 80, 8080, 443, 3128, 53, 21, 20]
ip = None
port = None
scan_type = None
open_ports = []
open_ports_count = 0
#Functions
def scan_port(ip, port): 
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if client.connect_ex((ip, port)):
            print(f"Port {port} is not open")
            return 0, {port}
        else:
            print(f"Port {port} open")
            return 1, {port}
    except socket.gaierror:
        print("Invalid IP!")
        input()
        exit()
    except OverflowError:
        print("Invalid port!")
        input()
        exit()


#Work
print("~Port Scanner 0.1")
ip = input("Please enter IP: ")
scan_type = input("Scan type (C - certain count ports, O - one port scan, F - most frequent ports): ").lower()

if scan_type == "f":
    for i in frequent_ports:
        op, p = scan_port(ip, i)
        open_ports_count += op
        if op == 1: open_ports += p
    print (f"Open ports detected: {open_ports_count}")
    action = input("S - show all ports, E - exit: ").lower()
    if action == "s":
        print(f"Open ports: {open_ports}")
        input()
        exit()
    else:
        exit()

elif scan_type == "o":
    try:
        port = int(input("Please enter port: "))
        if port > 65535:
            print("Error! Port must be 0-65535")
            input()
            exit()
        else:
            pass
    except ValueError:
        print("Invalid port!")
        input()
        exit()
    
    scan_port(ip, port)
    input()
    exit()
elif scan_type == "c":
    try:
        pcount = int(input("Please enter how many ports you want to scan: "))
        if pcount > 65535:
            print("Error! Max port count 65535")
            input()
            exit()
        else:
            pass
    except ValueError:
        print("Invalid port!")
        input()
        exit()

    for i in range(pcount + 1):
        op, p = scan_port(ip, i)
        open_ports_count += op
        if op == 1: open_ports += p
    print (f"Open ports detected: {open_ports_count}")
    action = input("S - show all ports, E - exit: ").lower()
    if action == "s":
        print(f"Open ports: {open_ports}")
        input()
        exit()
    else:
        exit()
else:
    print("Invalid argument!")