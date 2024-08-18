import os
import sys
from scapy.all import sniff, IP, TCP, UDP, Raw

def check_permissions():
   
    if os.geteuid() != 0:
        print("This script requires superuser privileges to capture network packets.")
        sys.exit(1)

def packet_callback(packet, show_payload):
    
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        print(f'\n[+] New Packet: {ip_src} -> {ip_dst} | Protocol: {protocol}')

        # Check for TCP packets
        if packet.haslayer(TCP):
            print(f'TCP Packet: {ip_src}:{packet[TCP].sport} -> {ip_dst}:{packet[TCP].dport}')
            if show_payload and packet.haslayer(Raw):
                print(f'Payload: {packet[Raw].load}')

        # Check for UDP packets
        elif packet.haslayer(UDP):
            print(f'UDP Packet: {ip_src}:{packet[UDP].sport} -> {ip_dst}:{packet[UDP].dport}')
            if show_payload and packet.haslayer(Raw):
                print(f'Payload: {packet[Raw].load}')

        else:
            print('Other Protocol')

def start_sniffing(interface=None, show_payload=False):
    print(f'Starting packet capture on {interface if interface else "all interfaces"}...')
    sniff(iface=interface, prn=lambda x: packet_callback(x, show_payload), store=False)

if __name__ == '__main__':
    
    check_permissions()
    
    # User input for interface
    interface = input('Enter the network interface to sniff on (leave blank for all interfaces): ')
    
    
    show_payload = input('Do you want to display payload data? (yes/no): ').strip().lower() == 'yes'
    
    # Start sniffing with the provided settings
    start_sniffing(interface, show_payload)
