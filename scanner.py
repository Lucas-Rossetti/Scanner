# Made by Gh0ST
# The use of this script is free
# Some information obtained by this script may be not reliable
# Enjoy

import sys, os, subprocess, socket
from colour import Color

# Parameters array
options = ['-l4', '-pt4', '-pt', '-a', '-h', '-v', '-o', '--help']

# Parameters's descriptions array
des = ['Lists all hosts addresses on the network(just the up ones !!! Feature not avaible yet !!!)', 'Shows the open ports(TCP) on a host', 'See if a specified port is open', 'Do a scan on all ports', 'Put the host address just after this option', 'Uses the verbose mode', 'Write the output to a file !!! Feature not avaible yet !!!', 'Shows this helping interface']

# Open ports array
ports = []

# Funtion to see a list of all up ips on the network
def l4():
    print("Scanning...")

# Funtion to scan all 1000 first TCP ports on an ipv4 (Verbose mode)
def pt4v(ip):
    print("Scanning...")
    for port in range(1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(port)
        conn = (ip, port)
        con = s.connect_ex(conn)
        s.close()
        if con == 0:
            ports.append(port)
            for d in range(5):
                print("Open port found!!! - ", port)
        else:
            pass

    if len(ports) == 0:
        print("No open ports found")

    else:
        print("Results for " + ip)
        print("Ports: ")
        print(ports)
        for a in ports:
            print(str(a) + " - open")

# Funtion to scan all TCP ports on an ipv4 (Verbose mode)
def pt4va(ip):
    print("Scanning...")
    for port in range(65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(port)
        conn = (ip, port)
        con = s.connect_ex(conn)
        s.close()
        if con == 0:
            ports.append(port)
            for d in range(5):
                print("Open port found!!! - ", port)
        else:
            pass

    if len(ports) == 0:
        print("No open ports found")

    else:
        print("Results for " + ip)
        print("Ports: ")
        print(ports)
        for a in ports:
            print(str(a) + " - open")

# Funtion to scan all TCP ports on an ipv4 (Normal mode)
def pt4a(ip):
    print("Scanning...")
    for port in range(65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(port)
        conn = (ip, port)
        con = s.connect_ex(conn)
        s.close()
        if con == 0:
            ports.append(port)
        else:
            pass

    if len(ports) == 0:
        print("No open ports found")

    else:
        print("Results for " + ip)
        print("Ports: ")
        print(ports)
        for a in ports:
            print(str(a) + " - open")

# Funtion to scan all 1000 first TCP ports on an ipv4 (Normal mode)
def pt4(ip):
    print("Scanning...")
    for port in range(1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = (ip, port)
        con = s.connect_ex(conn)
        s.close()
        if con == 0:
            ports.append(port)
        else:
            pass

    if len(ports) == 0:
        print("No open ports found")

    else:
        print("Results for " + ip)
        print("Ports:")
        for i in ports:
            print(str(i) + " - open")

# Function to see if a determined TCP port is open
def pt(ip, port):
    print("Scanning...")

    # Socket to connect
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Target address
    conn = (ip, port)

    # Connect and close the connection to see if it is up (open)
    con = s.connect_ex(conn)
    s.close()

    # See if the connection was succesful or not
    if con == 0:
        ports.append(port)
    else:
        pass

    # Print the obtained data
    if len(ports) == 0:
        print("Port is closed")

    else:
        print("Results for " + ip)
        print("Ports: ")
        for i in ports:
            print(str(i) + " - open")

# Redirection to the specified function. It is a mess =)
if "-l4" in sys.argv:
    l4()

elif "-pt4" in sys.argv:
    if "-v" in sys.argv:
        if "-a" in sys.argv:
            if "-h" in sys.argv:
                ip = sys.argv[sys.argv.index("-h")+1]
                pt4va(ip)

            else:
                print("No ip address")

        else:
            if "-h" in sys.argv:
                ip = sys.argv[sys.argv.index("-h")+1]
                pt4v(ip)

            else:
                print("No ip address")
    else:
        if "-a" in sys.argv:
            if "-h" in sys.argv:
                ip = sys.argv[sys.argv.index("-h")+1]
                pt4a(ip)

            else:
                print("No ip address")

        else:
            if "-h" in sys.argv:
                ip = sys.argv[sys.argv.index("-h")+1]
                pt4(ip)

            else:
                print("No ip address")

elif "-pt" in sys.argv:
    if "-h" in sys.argv:
        ip = sys.argv[sys.argv.index("-h")+1]
        port = int(sys.argv[sys.argv.index("-pt")+1])
        pt(ip, port)

elif "--help" in sys.argv:
    for i in range(len(options)):
        print(options[i] + " --> " + des[i])

    print("Example: python3 scanner.py -v -a -pt4 -h 127.0.0.1")
    print("Example: python3 scanner.py -pt 80 -h google.com")
    print("Obs: Using the verbose mode takes more time")
    print("Obs: Using the -pt4 option with the -a option, depending on the target, can take several minutes")
