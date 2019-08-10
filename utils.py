import re


def extract_list_of_bridges_specifications_from_file(path_to_bridges_file):

    list_of_bridges_sepcifications = [
        # "bridge1_ip, bridge1_key",
        # "bridge2_ip, bridge2_key",
    ]
    ip_regex_pattern = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

    with open(path_to_bridges_file, 'r') as file_:
        content = file_.readlines()

    for item in content:
        item = item.strip()
        if re.match(ip_regex_pattern, item):
            # remove extra spaces btwn ip and key
            bridge_specification = re.sub(" +", " ", item)
            list_of_bridges_sepcifications.append(bridge_specification)

    return list_of_bridges_sepcifications
