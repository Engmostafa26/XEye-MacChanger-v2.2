#! /usr/bin/env python
import optparse
import subprocess
import re
print(" \n*** Welcome to XEye Mac Changer, The most easiest Mac Changer tool ***")
def args():
    XEye = optparse.OptionParser()
    XEye.add_option("-i","--iface",dest="interface",help="Set the interface required to set new mac address for")
    XEye.add_option("-m","--mac",dest="mac",help="Set the required Mac address")
    (XEyee, XEyeee) = XEye.parse_args()
    if (not XEyee.interface) & (not XEyee.mac):
        Usermd()
        exit()
    if not XEyee.interface:
        XEye.error(" [Warning] --> no interface specified ..... Exiting")
        exit()
    if not XEyee.mac:
        XEye.error(" [Warning] --> no mac address specified ..... Exiting")
        exit()
    return XEyee

def Usermd():
    print("\n\n [Info] --> Entering the interactive mode ....")
    Interface = raw_input("\n         --> Enter the required Interface: ")
    if not Interface:
        print(" \n [Warning] --> No interface specified ..... Exiting")
        exit()
    Mac = raw_input("\n         --> Enter the required Mac address: ")
    if not Mac:
        print(" \n [Warning] --> No Mac address specified ..... Exiting")
        exit()
    Macc = getmac(Interface)
    if Macc == Mac:
        print(" \n [Info] --> You just entered the same Mac address for " + Interface + ", please enter a different mac ")
        exit()
    ChMac(Interface, Mac)
    Macc = getmac(Interface)
    if Macc == Mac:
        print(" [Done] --> The Mac Address is changed successfully to " + Mac)
        print(" \n [Author] --> Eng.Mostafa Ahmad - Cybersecurity Expert")
    else:
        print(" [Warning] --> Something Went wrong, The Mac Address didn't changed to "+Mac)
        print(" \n\n [Author] --> Eng.Mostafa Ahmad - Cybersecurity Expert")

def ChMac(Interface,Mac):
    subprocess.call(["ifconfig", Interface, "down"])
    subprocess.call(["ifconfig", Interface, "hw", "ether", Mac])
    subprocess.call(["ifconfig", Interface, "up"])
    print("\n [Info] --> XEye Mac Changer is setting your " + Interface + " Mac address to " + Mac)

def getmac(interface):
    ifconfgi_re = subprocess.check_output(["ifconfig", interface])
    testing1 = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfgi_re)
    testing2 = re.search(r"\w\w-\w\w-\w\w-\w\w-\w\w-\w\w", ifconfgi_re)
    if testing1:
        return testing1.group(0)
    elif testing2:
        return testing2.group(0)
    else:
        print("No Mac could be read")

def Run():
    XEyee = args()
    macc = getmac(XEyee.interface)
    if macc == XEyee.mac:
        print(" \n [Info] --> You just entered the same Mac address for " +XEyee.interface +", please enter a different Mac address ")
        print("\n")
        exit()
    ChMac(XEyee.interface, XEyee.mac)
    macc = getmac(XEyee.interface)
    if macc == XEyee.mac:
        print(" [Done] --> The Mac Address is changed successfully to " + str(macc))
    else:
        print(" [Warning] --> Something Went wrong, The Mac Address for "+XEyee.interface+" is not changed to "+XEyee.mac)

    print("\n *** Thanks for Using XEye Mac Changer ***")
    print(" \n [Author] --> Eng.Mostafa Ahmad - Cybersecurity Expert")
Run()
