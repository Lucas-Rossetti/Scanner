# Made by Lucas Rossetti
# The use of this script is free
# Some information obtained by this script ! may ! be not reliable
# Enjoy

# Imports
import sys, os, subprocess, socket, time
from datetime import datetime
from colorama import Fore, Style, init

# Parameters array
options = ['-l4', '-p4', '-p', '-a', '-d', '-h', '-v', '-o', 'install', '--help']

# Parameters's descriptions array
des = ['Lists all up host addresses on the network !!! Feature not avaible yet !!!', 'Shows the open ports(TCP) on a host', 'See if a specified port is open', 'Do a scan on all ports', 'Delay after p ports scanned t time. Example: -d 10 0.1 # Each 10 ports scanned, the program will delay 0.1 second', 'Put the host address just after this option', 'Uses the verbose mode', 'Write the output to a file !!! Feature not avaible yet !!!', 'Put this option if it is the first time your are using the scanner in your computer', 'Shows this helping interface']

# Call init function for Windows OS
init()

# Open ports array
ports = []

# Funtion to list all up IPs on the network
def l4(verbose):
    if verbose:
        print(Fore.GREEN + "[+] Scanning...")
        print(Fore.YELLOW + "[!] Feature not avaible yet")

    else:
        print(Fore.GREEN + "[+] Scanning...")
        print(Fore.YELLOW + "[!] Feature not avaible yet")

# Funtion to scan multiple ports on an IPV4 address
def p4(ip, al, verbose, delay):
    # Start
    start = datetime.now()

    # The number of ports to scan
    number = 65536 if al == True else 1000

    # Print "Scanning..."
    print(Fore.GREEN + "[+] Scanning...")
    print(Style.RESET_ALL)

    # Define t = 0
    t = 0

    # Do the scan
    for port in range(number):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = (ip, port)
        con = s.connect_ex(conn)
        s.close()
        if not verbose:
            if con:
                pass

            else:
                # Append the port into the ports array
                ports.append(port)

                # Print stuff
                print(Fore.GREEN + "[+] Open port found!!! -->", port, Style.RESET_ALL)
        else:
            # Prints on what port it is
            print(Fore.WHITE + str(port))

            # Sees if the connection was succesful or not
            if con:
                pass
            else:
                # Insert the port in an array of ports if the connection was succesful
                ports.append(port)

                # And prints the port
                print(Fore.GREEN + "[+] Open port found!!! -->", port)

        # Delay part
        if delay == ' ':
            pass

        else:
            if t == delay[0]:
                time.sleep(delay[1])
                t = 0

            else:
                t += 1
    # Finish
    finish = datetime.now()

    # Print results
    if len(ports) == 0:
        print(Fore.RED + "[-] No open ports found")

    else:
        print(Fore.GREEN + "[+] Results for " + ip + ":" + Style.RESET_ALL)
        print(number, "ports scanned in", finish - start)
        print(Fore.YELLOW + "[!] PORT | STATUS " + Fore.GREEN)
        for a in ports:
            print(str(a) + " --> open")

# Function to see if a determined TCP port is open
def p(ip, port, delay):
    print(Fore.GREEN + "[+] Scanning...")
    print(Style.RESET_ALL)

    # Socket to connect
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Target address
    conn = (ip, int(port))

    # Connect and close the connection to see if the port is open
    try:
        global con
        con = s.connect_ex(conn)
        s.close()

    # Throw an error if the port is invalid
    except OverflowError:
        print(Fore.YELLOW + "[!] Invalid port")
        print(Style.RESET_ALL)
        sys.exit()
        

    # See if the connection was succesful or not
    if con == 0:
        ports.append(port)
    else:
        pass

    # Print the obtained data
    if len(ports) == 0:
        print(Fore.RED + "[-] Port is closed")

    else:
        print(Fore.GREEN + "[+] Results for " + ip + ":")
        print(Fore.YELLOW + "[!] PORT | STATUS", Style.RESET_ALL)
        for i in ports:
            print(Fore.GREEN + str(i) + " --> open")
        print(Style.RESET_ALL)

# Redirection to the specified function. It is a mess, I am sorry =)
# Verification of verbose and all mode
verbose = True if '-v' in sys.argv else False
al = True if '-a' in sys.argv else False

# Sees if there is an IP address
if '-h' in sys.argv:
    try:
        global ip
        ip = sys.argv[sys.argv.index("-h") + 1]

    except:
        print(Fore.YELLOW + "[!] No IP address")
        sys.exit()

else:
    pass

# Takes the delay
delay = (int(sys.argv[sys.argv.index("-d") + 1]), float(sys.argv[sys.argv.index("-d") + 2])) if "-d" in sys.argv else ' '

if "-l4" in sys.argv:
    l4(verbose)

elif "-p4" in sys.argv:
    p4(ip, al, verbose, delay)

elif "-p" in sys.argv:
    p(ip, sys.argv[sys.argv.index("-p") + 1], delay)

elif "--help" in sys.argv:
    for i in range(len(options)):
        print(options[i] + " --> " + des[i])

    print("Example: python3 scanner.py -v -a -p4 -h 127.0.0.1 --> It will bring all open ports at 127.0.0.1\n")
    print("Example: python3 scanner.py -p 80 -h google.com --> It will check if the port 80 at google.com is open\n")
    print("Obs: Using the verbose mode takes more time")
    print("Obs: Using the -p4 option with the -a option, depending on the target, can take several minutes\n")
