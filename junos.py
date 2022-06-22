import time
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

try:
    usr = input("Enter your username: ") or "ntt-noc"
    pwd = getpass("Password: ")
except KeyboardInterrupt:   # exit when ctrl+c is pressed
    print("\nOK Good Bye!!!...")
    raise SystemExit

TimerStart = time.perf_counter()    # start timer

# Opening the file with IP addresses
with open("devices/devices.file") as f:
    devices_list = f.read().splitlines()

for device in devices_list:
    print("\n...Connecting to device " + device)
    ip_add = device
    device = {
        "device_type": "juniper",
        "ip": ip_add,
        "username": usr,
        "password": pwd,
    }
    try:
        action = ConnectHandler(**device)
    except (NetMikoTimeoutException):
        print("Device not reachable" + device)
        continue
    except (AuthenticationException):
        print("Authentication Failure: " + device)
        continue
    except (SSHException):
        print(
            "SSH does not seem to be enabled on "+device
        )
        continue
    except (Exception) as unknown_error:
        print(
            "\n There is some error \n\n\n"
            + unknown_error
        )
        continue
    try:
        print("\nConnected to " + device)
        bgp = action.send_command("sh bgp summary")
        for line in bgp.splitlines(): 
            if 'Down peers: 0' in line:
                print('BGP is UP')

            if 'Connect' in line or 'Idle' in line: 
                list_of_chunks = line.split(' ') 
                bgp_peer = list_of_chunks[0]  
                peer_status = list_of_chunks[-1] 
                bgp_time = list_of_chunks[7]
                print("BGP peer "+bgp_peer+" is "+peer_status+" for "+bgp_time+".\nCall Yannick on his mobile +31...")

        action.disconnect()

    except KeyboardInterrupt:
        print("Interupted by keyboad.")
        raise SystemExit

TimerEnd = time.perf_counter() # end timer
print(f"\nI did this in {TimerEnd - TimerStart:0.4f} seconds.\n")
