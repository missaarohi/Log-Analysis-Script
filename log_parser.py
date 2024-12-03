import re

def parse_log_file(file_path):
    log_data = []
    with open(file_path, 'r') as file:
        for line in file:
            match = re.match(r'(\d+\.\d+\.\d+\.\d+) - - .*?"(GET|POST) (.+?) HTTP.*?" (\d+) .*', line)
            if match:
                ip = match.group(1)
                method = match.group(2)
                endpoint = match.group(3)
                status_code = int(match.group(4))
                log_data.append({'ip': ip, 'method': method, 'endpoint': endpoint, 'status_code': status_code})
    return log_data

if __name__ == "__main__":
    logs = parse_log_file('sample.log')
    print("Parsed log entries:", logs)
