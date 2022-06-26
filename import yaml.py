import yaml
from ntc_templates.parse import parse_output

platform = 'juniper_junos'
command = 'show bgp summary'
raw_output_file = 'show_bgp_summary.raw'
data = open(raw_output_file, 'r').read()
parsed_output = parse_output(platform=platform, command=command, data=data)

# yaml.dump(parsed_output)
print(parsed_output)