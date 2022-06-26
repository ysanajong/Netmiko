# Example parsing output from Fortinet device get system status

get_sys_stat ="""Version: FortiGate-200E v6.4.9,build1966,220421 (GA)
Virus-DB: 90.03506(2022-06-22 22:20)
Extended DB: 90.03506(2022-06-22 22:19)
IPS-DB: 6.00741(2015-12-01 02:30)
IPS-ETDB: 21.00343(2022-06-21 23:50)
APP-DB: 21.00342(2022-06-21 00:49)
INDUSTRIAL-DB: 21.00342(2022-06-21 00:49)
IPS Malicious URL Database: 4.00389(2022-06-22 21:19)
Serial-Number: FG200ETK19902789
BIOS version: 05000006
System Part-Number: P19082-03
Log hard disk: Not available
Hostname: BE_LLN_FW_OT_11
Private Encryption: Disable
Operation Mode: NAT
Current virtual domain: root
Max number of virtual domains: 10
Virtual domains status: 1 in NAT mode, 0 in TP mode
Virtual domain configuration: disable
FIPS-CC mode: disable
Current HA mode: a-p, primary
Cluster uptime: 344 days, 17 hours, 12 minutes, 10 seconds
Cluster state change time: 2022-06-07 17:00:50
Branch point: 1966
Release Version Information: GA
FortiOS x86-64: Yes
System time: Thu Jun 23 11:34:55 2022"""
from ntc_templates.parse import parse_output

o_parsed = parse_output(platform="fortinet", command="get system status", data=get_sys_stat)
print (o_parsed)