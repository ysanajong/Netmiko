bgp_up_output = """
Threading mode: BGP I/O
Groups: 2 Peers: 6 Down peers: 0
"""
bgp_down_output = """
Groups: 2 Peers: 6 Down peers: 2
Peer                     AS      InPkt     OutPkt    OutQ   Flaps Last Up/Dwn State|#Active/Received/Accepted/Damped...
10.2.57.254           65252    1165670    1238837       0       1 9w2d 5:23:37 Idle
  wanTrusted.inet.0: 23/224/224/0
10.4.57.254           65252     753373     783304       0      50 35w2d 3:57:43 Idle
  wanTrusted.inet.0: 65/224/224/0
10.11.57.254          65252     814804     865022       0      19 6w3d 13:02:17 Establ
  wanTrusted.inet.0: 30/226/226/0
10.192.124.254        65252     768547     816071       0      47 36w5d 12:18:32 Establ
  wanUntrust.inet.0: 1/70/70/0
10.192.252.254        65252     811361     865023       0      20 6w3d 13:02:22 Establ
  wanUntrust.inet.0: 6/74/74/0
10.193.128.254        65252    1162649    1238837       0       1 9w2d 5:23:33 Establ
  wanUntrust.inet.0: 4/72/72/0
"""
from ntc_templates.parse import parse_output
from tabulate import tabulate

o_parsed = parse_output(platform="juniper_junos", command="show bgp summary", data=bgp_down_output)
o_parsed