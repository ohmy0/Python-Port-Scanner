import socket 

#Variables
frequent_ports = {
    20: "FTP-DATA", 21: "FTP", 22: "SSH", 23: "Telnet",
    25: "SMTP", 43: "WHOIS", 53: "DNS", 80: "http",
    115: "SFTP", 123: "NTP", 143: "IMAP", 161: "SNMP",
    179: "BGP", 443: "HTTPS", 445: "MICROSOFT-DS",
    514: "SYSLOG", 515: "PRINTER", 993: "IMAPS",
    995: "POP3S", 1080: "SOCKS", 1194: "OpenVPN",
    1433: "SQL Server", 1723: "PPTP", 3128: "HTTP",
    3268: "LDAP", 3306: "MySQL", 3389: "RDP",
    5432: "PostgreSQL", 5900: "VNC", 8080: "Tomcat", 10000: "Webmin" }
ip = None
port = None
scan_type = None
open_ports_count = 0
#Functions
def scan_port(ip, port): 
    try:
        client = socket.socket()
        client.settimeout(0.50)
        if client.connect_ex((ip, port)):
            return 0, {port}
        else:
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
print("~Port Scanner 1.0")
ip = input("Please enter IP: ")
scan_type = input("Scan type (C - certain count ports, O - one port scan, F - most frequent ports): ").lower()

if scan_type == "f":
    for i in frequent_ports:
        op, p = scan_port(ip, i)
        if op == 1: print(f"{frequent_ports[i]} | Open, port: {i}")
        open_ports_count += op
    print (f"Open ports detected: {open_ports_count}")
    action = input("E - exit: ").lower()
    if action == "e":
        exit()
    else:
        input()
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
    
    op, p = scan_port(ip, port)
    if op == 1: print(f"Port {port} open!")
    if op == 0: print(f"Port {port} is not open!")
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
        if op == 1: print(f"Port {i} open!")
    print (f"Open ports detected: {open_ports_count}")
    action = input("E - exit: ").lower()
    if action == "e":
        exit()
    else:
        input()
        exit()
else:
    print("Invalid argument!")