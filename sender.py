from scapy.all import *


with open('wg_byte.bin', 'rb') as payload_file:
    payload = payload_file.read()
    packet = IP(dst="158.160.19.239")/UDP(dport=12345)
    packet.add_payload(payload)
    send(packet)
    # send(IP(dst="158.160.19.239")/UDP(dport=12345)/Raw(load=payload_file.read()))