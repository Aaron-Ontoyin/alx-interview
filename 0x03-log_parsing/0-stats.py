#!/usr/bin/python3
"""Log parsing. Alx Interview questions"""
import re
import sys
# import signal


# def signal_handler(sig, frame):
#     """Handles keyboard Interupt"""
#     print_lines()
#     sys.exit(0)


def print_lines():
    """Prints available lines and filesize to stdout"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


# signal.signal(signal.SIGINT, signal_handler)

pattern = re.compile(
    r'(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] '
    r'"GET /projects/(\d+) HTTP/1\.1" (\d+) (\d+)'
)

total_file_size = 0
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

line_count = 0
try:
    for line in sys.stdin:
        line = line.strip()
        match = pattern.fullmatch(line)
        if match:
            size = int(match.group(5))
            status = int(match.group(4))

            total_file_size += size
            if status in status_codes:
                status_codes[status] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_lines()
finally:
    print_lines()
