import csv
from log_parser import parse_log_file
from analyze_requests import count_requests_per_ip
from most_accessed_endpoint import most_frequent_endpoint
from detect_suspicious import detect_suspicious_activity

def save_results_to_csv(file_name, log_data):
    ip_counts = count_requests_per_ip(log_data)
    endpoint, count = most_frequent_endpoint(log_data)
    suspicious_ips = detect_suspicious_activity(log_data)

    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)

        # Write Requests per IP
        writer.writerow(["IP Address", "Request Count"])
        writer.writerows(ip_counts)
        writer.writerow([])

        # Write Most Accessed Endpoint
        writer.writerow(["Most Accessed Endpoint", "Access Count"])
        writer.writerow([endpoint, count])
        writer.writerow([])

        # Write Suspicious Activity
        writer.writerow(["IP Address", "Failed Login Count"])
        writer.writerows(suspicious_ips)

if __name__ == "__main__":
    logs = parse_log_file('sample.log')
    save_results_to_csv('log_analysis_results.csv', logs)
    print("Results saved to log_analysis_results.csv")
