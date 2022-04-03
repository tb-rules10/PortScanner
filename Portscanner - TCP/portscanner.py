import socket
import termcolor
import time

n = 0
open_port = []

def scan(ipad, ports):
    ind = ports.find('-')
    r1,r2 = int(ports[0:ind]), int(ports[ind+1:])
    scan = r2-r1+1
    open_port.clear()
    for port in range(r1,r2+1):
        scan_port(ipad, port)
    open = len(open_port)
    print()
    print(scan," Ports Scanned")
    print(open," Open Ports & ",(scan-open),"Closed Ports Found")

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened : "+str(port))
        open_port.append(str(port))
        sock.close()
    except: 
        # print("[-] Port Closed : "+str(port))
        pass

targets = input("\n[*] Enter Targets To Scan (separated by a space ' ' if multiple) : ")
ports = input("[*] Enter Range Of Ports To Be Scanned (separated by hyphen) : ")
if " " in targets:
    print("\n",termcolor.colored(("[*] Scanning Multiple Targets :-"), 'green'))
    target = targets.split(" ")
    start = time.time()
    for ipad in target:
        print("\n------Starting Scan For ",ipad,"------\n")
        scan(ipad, ports)
    ip_count = len(target)
else:
    print("\n------Starting Scan For ",targets,"------\n")
    start = time.time()
    scan(targets,ports)
    ip_count = 1

end = time.time()
print("\n---------------------------------------------\n")
print(termcolor.colored(("Scanning Done : "), 'green'),ip_count,termcolor.colored((" IP Address Scanned In "), 'green'),end='')
print(termcolor.colored((f' {end-start:.2f} seconds\n'), 'green'))
