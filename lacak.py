import socket
from termcolor import colored
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance

# header
print('=' * 27)
print(colored("[?] Lacak IP By : Santri IT",'green'))
print('=' * 27)

# proses
def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print("")
    print(f"IP address : {res.ip_address}")
    print(f"Lokasi : {res.city},{res.region},{res.country}")
    print(f"Coordinat : (lat: {res.latitude}, Lng : {res.longitude})")

ip_add = input(colored("[?] Enter IP : ",'red'))
printDetails(ip_add)
