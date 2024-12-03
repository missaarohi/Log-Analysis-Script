from log_parser import parse_log_file
from collections import Counter

def count_requests_per_ip(log_data):
    ip_counts = Counter(entry['ip'] for entry in log_data)
    return ip_counts.most_common()

if __name__ == "__main__":
    logs = parse_log_file('sample.log')
    ip_counts = count_requests_per_ip(logs)
    print("IP Address         Request Count")
    for ip, count in ip_counts:
        print(f"{ip:<17} {count}")
