print("""
██████╗  ██████╗ ██████╗ ████████╗
██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
██████╔╝██║   ██║██████╔╝   ██║
██╔═══╝ ██║   ██║██╔══██╗   ██║
██║     ╚██████╔╝██║  ██║   ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝

        PYTHON PORT SCANNER
""")

import socket

PORT_NAME = {
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    80: "HTTP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

for port in PORT_NAME:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    status = s.connect_ex(("127.0.0.1", port))

    if status == 0:
        print(f"Port {port} ({PORT_NAME[port]}) is OPEN")
    else:
        print(f"Port {port} ({PORT_NAME[port]}) is CLOSED")

    s.close()