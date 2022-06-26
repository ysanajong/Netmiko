import textfsm
import json

template_file = 'juniper_junos_show_bgp_summary.textfsm'
raw_output_file = 'show_bgp_summary.raw'

with open(template_file) as fd_t, open(raw_output_file) as fd_o:
    re_table = textfsm.TextFSM(fd_t)
    parsed_header = re_table.header
    parsed_output = re_table.ParseText(fd_o.read())

print(json.dumps(parsed_header))
print(json.dumps(parsed_output))