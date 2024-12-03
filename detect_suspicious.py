from log_parser import parse_log_file
from collections import Counter

def detect_suspicious_activity(log_data, threshold=10):
    failed_attempts = Counter(entry['ip'] for entry in log_data if entry['status_code'] == 401)
    return [(ip, count) for ip, count in failed_attempts.items() if count > threshold]

if __name__ == "__main__":
    logs = parse_log_file('sample.log')
    suspicious_ips = detect_suspicious_activity(logs)
    print("Suspicious Activity Detected:")
    print("IP Address         Failed Login Attempts")
    for ip, count in suspicious_ips:
        print(f"{ip:<17} {count}")
