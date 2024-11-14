import scapy.all as scapy

# Packet handler function to process each captured packet
def packet_callback(packet):
    # Display some basic packet information
    print(f"Packet: {packet.summary()}")
    
    # If it's an IP packet, print detailed information
    if packet.haslayer(scapy.IP):
        ip_src = packet[scapy.IP].src
        ip_dst = packet[scapy.IP].dst
        print(f"IP Packet: {ip_src} -> {ip_dst}")
        
        # Check if the packet has a TCP layer (optional)
        if packet.haslayer(scapy.TCP):
            tcp_sport = packet[scapy.TCP].sport
            tcp_dport = packet[scapy.TCP].dport
            print(f"TCP Packet: {tcp_sport} -> {tcp_dport}")
        
        # Check if the packet has a UDP layer (optional)
        elif packet.haslayer(scapy.UDP):
            udp_sport = packet[scapy.UDP].sport
            udp_dport = packet[scapy.UDP].dport
            print(f"UDP Packet: {udp_sport} -> {udp_dport}")

# Start sniffing the network on the specified interface
def start_sniffing(interface="Wi-Fi"):  # Replace with your network interface name
    print(f"Sniffing on interface: {interface}...")
    scapy.sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    # Start sniffing on the specified interface (e.g., "Ethernet", "Wi-Fi")
    start_sniffing("Wi-Fi")  # Adjust this to match your system's interface name
