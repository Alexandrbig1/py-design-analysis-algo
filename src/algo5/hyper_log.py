import argparse
import json
import time
from datasketch import HyperLogLog


def load_ip_addresses(filename):
    ip_addresses = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                log_entry = json.loads(line)
                if 'remote_addr' in log_entry:
                    ip_addresses.append(log_entry['remote_addr'])
            except json.JSONDecodeError:
                continue
    return ip_addresses

def count_unique_ips_set(ip_addresses):
    return len(set(ip_addresses))

def count_unique_ips_hll(ip_addresses, precision=12):
    hll = HyperLogLog(precision)
    for ip in ip_addresses:
        hll.update(ip.encode('utf-8'))
    return len(hll)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str, nargs='?', default='lms-stage-access.log', help='Path to file')
    args = parser.parse_args()

    ip_addresses = load_ip_addresses(args.filename)

    start_time = time.time()
    exact_count = count_unique_ips_set(ip_addresses)
    exact_time = time.time() - start_time

    start_time = time.time()
    hyper_log_log_count = count_unique_ips_hll(ip_addresses)
    hyper_log_log_time = time.time() - start_time

    print("Comparison results:")
    print(f"{'':20}Exact count   HyperLogLog")
    print(f"{'Unique elements':20}{exact_count:<15.1f}{hyper_log_log_count:<15.1f}")
    print(f"{'Execution time (sec.)':20}{exact_time:<15.3f}{hyper_log_log_time:<15.3f}")
    print(f"Loaded IP addresses: {len(ip_addresses)}")


if __name__ == '__main__':
    main()