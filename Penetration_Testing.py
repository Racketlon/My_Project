'''
This Python program is a tool with most used tool for penetration testing (ethical hacking).
The idea is, how you can create these tools in python and what you can do nowadays with these tools.
This all in one tool is only for educational purpose.
'''

import itertools  # module for combinatorial iterators
import os  # module for os (operating system)
import socket  # module for network communication
import time  # module for time

import netifaces  # module for network interface information
import psutil  # module for system information
import pyfiglet  # module for title in design font
from colorama import Fore  # module for font color change
from phonenumbers import (  # module for phonenumbers 
    carrier,
    geocoder,
    parse,
    region_code_for_number,
)


def one_row_printing(text):
    '''
    This function prints texts in one row with animation
    '''

    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.1)  # Adjust the delay as needed
    print('\n') 
    time.sleep(1)


def clear_console():
    '''
    This function clears the console for better overview
    '''

    os.system('cls')  # Clear console for Windows

def local_scanner():
    def get_ip_address():
        '''
        This function gathers the IP addresses of the active hosts on the network.
        '''

        clear_console()
        print(pyfiglet.figlet_format('IP Address'))
        time.sleep(1)
        one_row_printing('[*] Connecting to your device')
        one_row_printing('[*] Getting IP addresses of your device')
        ip_addresses = [] # define ip_addresses as a list
        interfaces = netifaces.interfaces() # get list of all network interfaces abailable on the system using netifaces
        for interface in interfaces:
            addresses = netifaces.ifaddresses(interface) # define addresses with the given network interface
            if netifaces.AF_INET in addresses: # check if interface has IPv4
                for link in addresses[netifaces.AF_INET]: # loop each IPv4 with interface
                    ip_address = link['addr'] # extract ip address
                    ip_addresses.append(ip_address) # append ip address
                    time.sleep(0.5)

        print("IP addresses on the network:")
        for ip in ip_addresses:
            print(ip)
        print('\n')

    def get_names_of_IP():
        '''
        This function gathers the names of the IP addresses
        '''

        clear_console()
        print(pyfiglet.figlet_format('Names of IP'))
        time.sleep(1)
        one_row_printing('[*] Connecting to your device')
        one_row_printing('[*] Getting names of IP addresses of your device')    
        ip_addresses = [] # define ip_addresses as a list
        interfaces = netifaces.interfaces() # get list of all network interfaces abailable on the system using netifaces
        for interface in interfaces:
            addresses = netifaces.ifaddresses(interface) # define addresses with the given network interface
            if netifaces.AF_INET in addresses: # check if interface has IPv4
                for link in addresses[netifaces.AF_INET]: # loop each IPv4 with interface
                    ip_address = link['addr'] # extract ip address
                    try:
                        interface_name = psutil.net_if_addrs()[interface][0].address # get address with specified netword interface using psutil
                    except:
                        interface_name = interface # define interface_name
                    ip_info = {'name': interface_name, 'ip': ip_address}
                    ip_addresses.append(ip_info) # append ip info

        print("Names of IP addresses on the network:")
        for ip in ip_addresses:
            print(ip)
        print('\n')

    def get_mac_address():
        '''
        This function gathers the MAC addresses of the active hosts on the network.
        '''

        clear_console()
        print(pyfiglet.figlet_format('MAC addresses'))
        time.sleep(1)
        one_row_printing('[*] Connecting to your device')
        one_row_printing('[*] Getting MAC addresses of your device')
        interfaces = netifaces.interfaces() # get list of all network interfaces abailable on the system using netifaces
        for interface in interfaces: # loop for each network interface
            addresses = netifaces.ifaddresses(interface) # get addresses of current network interface
            if netifaces.AF_LINK in addresses and netifaces.AF_INET in addresses: # check if IPv4 and MAC addresses are available
                mac_address = addresses[netifaces.AF_LINK][0]['addr'] # get MAC address with interface
                ip_address = addresses[netifaces.AF_INET][0]['addr'] # get IPv4 address with interface
                print(f"MAC address: {mac_address} IP address: {ip_address}\n")


    def get_open_ports():
        '''
        This function returns the status of ports on every IP address
        '''

        clear_console()

        # Define a dictionary mapping port numbers to their service names
        ports = {
        1: 'TCPMUX',
        5: 'Remote Job Entry',
        7: 'Echo Protocol',
        9: 'Discard Protocol',
        13: 'Daytime Protocol',
        17: 'Quote of the Day',
        18: 'Message Send Protocol',
        19: 'Character Generator Protocol',
        20: 'FTP Data Transfer',
        21: 'FTP Control',
        22: 'SSH',
        23: 'Telnet',
        25: 'SMTP',
        37: 'Time Protocol',
        42: 'Host Name Server',
        43: 'WHOIS',
        49: 'Login Host Protocol',
        53: 'DNS',
        69: 'TFTP',
        70: 'Gopher',
        79: 'Finger',
        80: 'HTTP',
        88: 'Kerberos',
        101: 'NIC Host Name Server',
        102: 'ISO-TSAP',
        107: 'Remote Telnet Service',
        109: 'POP2',
        110: 'POP3',
        115: 'SFTP',
        118: 'SQL Services',
        119: 'NNTP',
        123: 'NTP',
        137: 'NetBIOS Name Service',
        138: 'NetBIOS Datagram Service',
        139: 'NetBIOS Session Service',
        143: 'IMAP',
        156: 'SQL Service',
        161: 'SNMP',
        179: 'BGP',
        190: 'GACP',
        194: 'IRC',
        197: 'DLS',
        389: 'LDAP',
        396: 'Novell Netware over IP',
        443: 'HTTPS',
        444: 'SNPP',
        445: 'Microsoft-DS',
        458: 'Apple QuickTime',
        546: 'DHCP Client',
        547: 'DHCP Server',
        563: 'NNTPS',
        569: 'MSN',
        1080: 'Socks Proxy',
        1433: 'Microsoft SQL Server',
        1434: 'Microsoft SQL Monitor',
        1494: 'Citrix',
        1521: 'Oracle',
        1720: 'H.323',
        1723: 'PPTP',
        1863: 'MSN Messenger',
        2082: 'cPanel',
        2083: 'cPanel SSL',
        3306: 'MySQL',
        3389: 'Remote Desktop Protocol',
        5900: 'VNC Server',
        8080: 'HTTP Alternate',
        }

        print(pyfiglet.figlet_format('Open ports'))
        time.sleep(1)
        one_row_printing('[*] Connecting to your device')
        one_row_printing('[*] Getting open ports of IP addresses of your device')
        interfaces = netifaces.interfaces() # get list of all network interfaces abailable on the system using netifaces
        for interface in interfaces: # loop for each network interface
            addresses = netifaces.ifaddresses(interface) # get addresses of current network interface
            if netifaces.AF_INET in addresses:  # check if interface has IPv4
                ip_address = addresses[netifaces.AF_INET][0]['addr'] # get IPv4 address with interface
                print(f"Interface: {interface}\nIP address: {ip_address}\n")
                for port in ports: # loop for each port
                    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # create a TCP socket
                        s.settimeout(1)  # Set timeout for connection attempt
                        result = s.connect_ex((ip_address, port)) # attempt to connect to IP and port
                        if result == 0:  # Port is open
                            service_name = ports[port] if port in ports else 'Unknown' # get service name with port else return Unknown
                            print(f"Port: {port}\nService: {service_name}\n")


    clear_console()
    print(pyfiglet.figlet_format('Network Scanner'))
    option = int(input('[01] Get IP addresses\n[02] Get names of IP addresses\n[03] Get MAC addresses\n[04] Get open ports\n[99] Back\nYour option: '))
    if option == 1:
        get_ip_address()
    elif option == 2:
        get_names_of_IP()
    elif option == 3:
        get_mac_address()
    elif option == 4:
        get_open_ports()
    elif option == 99:
        main()
    else:
        clear_console()
        local_scanner()

def phonenumber_func():
    def location():
        '''
        This function gathers the location of the phone number.
        '''
        clear_console()
        print(pyfiglet.figlet_format('Locator'))

        # taking input the phonenumber along with the country code
        number = input("Enter the PhoneNumber with the country code : ")

        # Parsing the phonenumber string to convert it into phonenumber format
        phoneNumber = parse(number, None)

        print('\n')
        time.sleep(1)
        one_row_printing('[*] Connecting to the given phonenumber')
        one_row_printing('[*] Trying to locate the given phonenumber')

        # Using the geocoder module of phonenumbers to print the Location in console
        yourLocation = geocoder.description_for_number(phoneNumber,"en")
        print("location : "+yourLocation)
        print('\n')

    def provider():
        '''
        This function gathers the provider of the phone number.
        '''
        clear_console()
        print(pyfiglet.figlet_format('Provider'))

        # taking input the phonenumber along with the country code
        number = input("Enter the PhoneNumber with the country code : ")
        # Parsing the phonenumber string to convert it into phonenumber format
        phoneNumber = parse(number, None)

        print('\n')
        time.sleep(1)
        one_row_printing('[*] Connecting to the given phonenumber')
        one_row_printing('[*] Trying to find the provider of the given phonenumber')

        # Using the carrier module of phonenumbers to print the service provider name in console
        yourServiceProvider = carrier.name_for_number(phoneNumber,"en")
        print("service provider : "+yourServiceProvider)
        print('\n')

    def nation():
        '''
        This function determines the nation (e.g., +41, CH) of the phone number.
        '''
        clear_console()
        print(pyfiglet.figlet_format('Nation'))

        # taking input the phonenumber along with the country code
        number = input("Enter the PhoneNumber with the country code : ")
        # Parsing the phonenumber string to convert it into phonenumber format
        phoneNumber = parse(number, None)

        print('\n')
        time.sleep(1)
        one_row_printing('[*] Connecting to the given phonenumber')
        one_row_printing('[*] Trying to find the nation of the given phonenumber')

        nation = region_code_for_number(phoneNumber)
        if nation is not None:
            print("Nation (Country code): " + nation)
        else:
            print("Unable to determine the nation from the phone number.")
        print('\n')

    clear_console()
    print(pyfiglet.figlet_format('Phonenumbers'))
    option = int(input('[01] Get location\n[02] Get provider\n[03] Get nation\n[99] Back\nYour option: '))

    if option == 1:
        location()
    elif option == 2:
        provider()
    elif option == 3:
        nation()
    elif option == 99:
        main()
    else:
        clear_console()
        phonenumber_func()

def password_checker():
    def brute_force():
        '''
        This function performs a brute-force attack to crack the given password.
        '''
        clear_console()
        print(pyfiglet.figlet_format('Brute Force'))

        # Define the password
        password = input('Enter the target password: ')

        # Define the character
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+'

        print('\n')
        text_1 = '[*] Trying to brute force the entered password'
        text_2 = '[*] This may take a few time'
        time.sleep(1)
        for letter in text_1:
            print(letter, end='', flush=True)
            time.sleep(0.1)  # printing each letter after 0.1 seconds
        print('\n')
        time.sleep(1)
        for letter in text_2:
            print(letter, end = '', flush=True)
            time.sleep(0.1)
        time.sleep(1)
        print('\n')

        # Start the timer
        start_time = time.time()

        # Iterate through all possible password combinations
        for length in range(1, len(password) + 1):
            for attempt in itertools.product(characters, repeat=length): # generate all possible combinations of characters with specified length
                if len(''.join(attempt)) == len(password):  # Check length to avoid joining characters that exceed the password length
                    brute_password = ''.join(attempt)
                    if brute_password == password:
                        # Password cracked
                        end_time = time.time()
                        time_taken = end_time - start_time
                        print(f"Password cracked: {brute_password}")
                        print(f"Time taken: {time_taken:.2f} seconds") # give seconds with two digits 
                        print('\n')
                        return  # Exit function if password is cracked

        # If the password is not cracked after trying all combinations
        print("Failed to crack the password.")

    clear_console()
    print(pyfiglet.figlet_format('Password checker'))
    option = int(input('[01] Brute Force\n[99] Back\nYour option: '))

    if option == 1:
        brute_force()
    elif option == 99:
        main()
    else:
        clear_console()
        password_checker()


def website():
    def get_open_ports():
        '''
        This function returns the status of ports of a website.
        '''

        clear_console()
        print(pyfiglet.figlet_format('Ports'))

        # define the host url
        hosts = input('Enter the website: ')

        # define the ports
        ports = {
                21 : 'FTP',
                22 : 'SSH',
                23 : 'Telnet',
                25 : 'SMTP',
                80 : 'HTTP',
                110 : 'POP3',
                143 : 'IMAP',
                443 : 'HTTPS',
                3306 : 'MySQL',
                5432 : 'PostgreSQL',
                }
        timeout_seconds=1

        print('\n')
        time.sleep(1)
        one_row_printing('[*] Connecting to the given website')
        one_row_printing('[*] Scanning the status of ports')

        for host in hosts.split():  # Split hosts by spaces if multiple provided
            host = host.rstrip("\n")
            try:
                ip = socket.gethostbyname(host)
            except socket.gaierror as e:
                print(f"Error: {e}. Skipping host: {host}")
                continue

            for port, service in ports.items():
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(timeout_seconds) # setting timeout to 1 second
                try:
                    result = sock.connect_ex((ip, port)) # checks the connection of ip and port
                    if result == 0:
                        print("Host: {}, Port: {}, Service: {}, Status: Open".format(host, port, service)) # prints names in {} by using .format() and returns if status is open
                    else:
                        print("Host: {}, Port: {}, Service: {}, Status: Closed".format(host, port, service)) # prints names in {} by using .format() and returns if status is closed
                except Exception as e:
                    print(f"Error occurred while scanning port {port} on host {host}: {e}") # prints error on port and host and the error code
                finally:
                    sock.close()
        print('\n')

    clear_console()
    print(pyfiglet.figlet_format('Website'))
    option = int(input('[01] Open ports\n[99] Back\nYour option: '))

    if option == 1:
        get_open_ports()
    elif option == 99:
        main()
    else:
        clear_console()
        website()


def about_us():
    '''
    This function provides information about the tool and its creators.
    '''

    print(pyfiglet.figlet_format('About'))
    print('This is an all-in-one tool for penetration testing. It was created by Jamie, Philipp and Andreas. The project was to create a python script that can be used for information gathering. It is only designed for educational purposes not for hacking!')
    print('\n')

    option_back = int(input('[99] Back\nYour option: '))
    if option_back == 99:
        main()
    else:
        clear_console()
        about_us()

def main():
    clear_console()
    print(f'{Fore.GREEN}') # setting font color to green
    print(pyfiglet.figlet_format('Penetration Testing'))
    print(f"{Fore.RED}Do not use it for illegal purposes!{Fore.GREEN}") # printing text in red then in green
    while True:
        option = int(input('[01] Local networks\n[02] Phonenumber\n[03] Password checker\n[04] Port scanner\n[05] About\n[99] Exit\nYour option: '))
        clear_console()
        if option == 1:
            clear_console()
            local_scanner()
        elif option == 2:
            clear_console()
            phonenumber_func()
        elif option == 3:
            clear_console()
            password_checker()
        elif option == 4:
            clear_console()
            website()
        elif option == 5:
            clear_console()
            about_us()
        elif option == 99:
            text = 'Thank you for using this tool!'
            for letter in text:
                print(letter, end='', flush=True)
                time.sleep(0.1)  # printing each letter after 0.1 seconds
            time.sleep(1)
            exit()
        else:
            clear_console()
            main()

if __name__ == "__main__":
    main()