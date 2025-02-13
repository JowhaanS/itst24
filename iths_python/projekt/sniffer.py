from scapy.all import sniff, wrpcap

def sniff_packets(interface, count, bpf_filter, output_file, verbose):
    print(f"[*] Sniffing on interface {interface} with filter '{bpf_filter}'")

    def packet_handler(packet):
        if verbose:
            packet.show()
        else:
            print(f"Packet captured: {packet.summary()}")

    packets = sniff(iface=interface, filter=bpf_filter, count=count, prn=packet_handler)
    
    #Adding the pcap suffix
    if output_file:
        wrpcap(f"{output_file}.pcap", packets)
        print(f"[*] Saved {len(packets)} packets to {output_file}.pcap")
