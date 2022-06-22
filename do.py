import time
# from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

TimerStart = time.perf_counter()    # start timer
""" try:
    usr = input("Enter your username: ") or "ntt-noc"
    # pwd = getpass("Password: ") 
    pwd = "554297nHH"

except KeyboardInterrupt:   # exit when ctrl+c is pressed
    print("\nOK Bye!!!...")
    raise SystemExit """

usr = "yms"
    # pwd = getpass("Password: ") 
pwd = "554297nHH"

# TimerStart = time.perf_counter()    # start timer

# Opening the file with IP addresses
with open("devices.file") as f:
    devices_list = f.read().splitlines()

for device in devices_list:
    print("\n...Connecting to device " + device)
    ip_add = device
    device = {
        "device_type": "linux",
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
            "\n There is some error, do not panick. Contact Yannick \n\n\n"
            + unknown_error
        )
        continue
    except KeyboardInterrupt:
        print("\nOK Bye!!!...")
        raise SystemExit

    try:
        cmd_hostname = action.send_command("hostname")
        print("\nConnected to " + cmd_hostname)
        cmd_df = action.send_command("df -H")
        action.disconnect()
        print("\nCurrent Disk Usge is:")
        print(cmd_df)
    except KeyboardInterrupt:
        print("Interupted by keyboad.")
        raise SystemExit

TimerEnd = time.perf_counter() # end timer
print(f"\nI did thi in {TimerEnd - TimerStart:0.4f} seconds.\n")
