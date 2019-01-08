"""
Create a CSV file from ifconfig data as follows:
interface,inet,status
lo0,127.0.0.1,
gif0,,
en0,10.176.85.19,active
en1,,inactive
p2p0,,inactive
"""

import subprocess
import re

network = subprocess.check_output(['ifconfig'])

network_data = {

        'lo0': '',
        'gif0': '',
        'en0': '',
        'en1': '',
        'p2p0': '',
}

print network

for n in network.split('\n\n'):


        inet = re.search( r'inet\s\w+[127].\d.\d.\d', n)
        if inet:
                network_data['lo0'] = inet.group().split('inet ')[-1]
        gif0 = re.search( r'gif0', n)
        if gif0:
                network_data['gif0'] = ''
        en0 = re.search(r'inet\s\w+\d+.\d.\d.\d', n)
        if en0:
                network_data['en0'] = en0.group().split('inet ')[-1]

print(network_data)

print re.findall(r'^(\S+).*?inet addr:(\S+).*?Mask:(\S+)', network, re.S | re.M)
[('eth0', '192.168.98.157', '255.255.255.0'), ('lo', '127.0.0.1', '255.0.0.0')]
