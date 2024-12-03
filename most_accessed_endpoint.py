from log_parser import parse_log_file
from collections import Counter

def most_frequent_endpoint(log_data):
    endpoint_counts = Counter(entry['endpoint'] for entry in log_data)
    return endpoint_counts.most_common(1)[0]

if __name__ == "__main__":
    logs = parse_log_file('sample.log')
    endpoint, count = most_frequent_endpoint(logs)
    print("Most Frequently Accessed Endpoint:")
    print(f"{endpoint} (Accessed {count} times)")
