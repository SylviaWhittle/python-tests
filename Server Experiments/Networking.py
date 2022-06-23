# import socket

# UDP_IP = "raspi4"
# UDP_PORT = "5005"
# MESSAGE = "Hello, world"

# # Set up UDP
# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # Send UDP packet
# sock.sendto(bytes(MESSAGE, "utf-8"), (UDP_IP, UDP_PORT))


import socket
import sys
import time
import psutil
import subprocess
import datetime
import os

psscript = """
$t = Get-WmiObject MSAcpi_ThermalZoneTemperature -Namespace “root/wmi”

while (1) {$t.CurrentTemperature; sleep 5}
"""

si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW

cmd = ["powershell.exe", "-Command", psscript]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, startupinfo=si)

print(str(proc.stdout.readline()))


# with open(r"C:\Users\skyradar\Desktop\temp.txt", "w") as fd:
#     while True:
#         tmp = proc.stdout.readline()
#         proc.stdout.readline()  # hack to prevent output twice
#         celsius = int(tmp) / 10 - 273.15
#         celsius_str = f"{celsius:.2f};{datetime.datetime.now().isoformat()}"
#         print(celsius_str)
#         fd.write(celsius_str)
#         fd.write(os.linesep)

# while True:
#     time.sleep(0.1)
#     print(psutil.sensors_temperatures())


# if len(sys.argv) == 3:
#     # Get "IP address of Server" and also the "port number" from argument 1 and argument 2
#     ip = sys.argv[1]
#     port = int(sys.argv[2])
# else:
#     print(
#         "Run like : python3 client.py <arg1 server ip 192.168.1.102> <arg2 server port 4444 >"
#     )
#     exit(1)

# server_hostname = "raspi4"
# server_ip_address = socket.gethostbyname(server_hostname)
# port = 5005

# # Create socket for server
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
# print("Do Ctrl+c to exit the program !!")


# i = 0
# while True:
#     s.sendto(str(i).encode("utf-8"), (server_ip_address, port))
#     i += 1
#     time.sleep(0.5)

# # Let's send data through UDP protocol
# while True:
#     send_data = input("Type some text to send =>")
#     s.sendto(send_data.encode("utf-8"), (server_ip_address, port))
#     print("\n\n 1. Client Sent : ", send_data, "\n\n")
#     data, address = s.recvfrom(4096)
#     print("\n\n 2. Client received : ", data.decode("utf-8"), "\n\n")
# # close the socket
# s.close()
