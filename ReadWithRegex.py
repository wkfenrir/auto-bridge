#this code will finde IPs from text
import re
​
​
def extract_ip_from_bridge_file(path_to_bridges_file):
    ip_regex_pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")
​
    with open(path_to_bridges_file, 'r') as file_:
        content = file_.readlines()
​
    for item in content:
        item = item.strip()
        if re.match(ip_regex_pattern, item):
            # split each item with space and first index of each list is ip
            ip = item.split()[0]
            print(ip)