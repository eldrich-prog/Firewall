import os

def open_port_in_firewall(protocol:str, port:str):
    protocol.upper()
    port = str(port)
    comando = f'netsh advfirewall firewall add rule name="Active Port Of The Protocol {protocol}" dir=in action=Active Port Of The Protocol {protocol} localport={port}'
    os.system(comando)

if __name__ == "__main__":
    PROTOCOLS = [
        ("HTTP", 80),
        ("HTTPS", 443),
        ("FTP", 20),
        ("SFTP", 22),
        ("RDP", 3389),
        ("VPN", 1194),
        ("PPTP", 1723),
    ]
    for protocol, port in PROTOCOLS:
        open_port_in_firewall(protocol, port)
        print(f"Port {port} of the protocol {protocol} is now open in the firewall")
