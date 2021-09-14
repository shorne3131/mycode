#!/usr/bin/env python3
## USOpen Tournament Switch Checker -- 2018.05.01

''' usopen.py
This script is being designed to provide the following automated tasks:
- Ping check the router (import os)
- Login check the router (import netmiko)
- Determine if interfaces in use are up (import netmiko)
- Apply new configuration (import netmiko) # not yet built

The IPs and device type should be made available via a csv spreadsheet

'''

import os

## pyexcel and pyexcel-xls are required for our program to execute
# python3 -m pip install --user pyexcel
# python3 -m pip install --user pyexcel-xls
import pyexcel
from netmiko import ConnectHandler

## retrieve data set from spreadsheet
def retv_excel(par):
    d = {}
    # create a record object that is an open spreadsheet
    records = pyexcel.iget_records(file_name=par)
    for record in records:
        # adds a new IP and driver key:value pair to our dictionary
        d.update( { record['IP'] : record['driver'] } )
    return d # return the completed dictionary

# there is no function named interface_check is the issue
# looks like you combined the login_router() and interface_check() functions into one
# you can delete lines 50-52 and change the name of this function to interface_check and that will fix it!

def login_router(dev_type, dev_ip, dev_un, dev_pw):
    open_connection= ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pw)

def interface_check(dev_type, dev_ip, dev_un, dev_pw):
    open_connection= ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pw)
    my_command= open_connection.send_command("show ip int brief")
    print(my_command)

def main():

    ## Determine where *.csv input is
    file_location = input("\nWhere is the file location? ")

    ##Entry is now a local dictionary containing IP(key):driver(value)
    entry= retv_excel(file_location)

    print("\n***** BEGIN SSH CHECKING *****")
    for x in entry.keys():
        print(entry[x])
        login_router(entry[x], x, "admin", "alta3")

    for x in entry.keys():
            os.system("ping -c 2 " + x)

    for x in entry.keys():
        os.system("ping -c 1 " +x)

    for x in entry.keys():
        interface_check(entry[x], x, "admin", "alta3")

main()
