import getpass
import telnetlib

HOST = "192.168.0.200"
user = input("Enter your Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
tn.write(b"vlan 2\n")
tn.write(b"name v2\n")
tn.write(b"vlan 3\n")
tn.write(b"name v3\n")
tn.write(b"end 2\n")
tn.write(b"exit 2\n")
print(tn.read_all().decode('ascii'))
