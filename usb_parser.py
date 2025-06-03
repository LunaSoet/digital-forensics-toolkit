# forensics/usb_parser.py
import re

def parse_usb_logs(log_file):
    try:
        with open(log_file, 'r') as f:
            lines = f.readlines()
        usb_events = [line for line in lines if 'usb' in line.lower()]
        return usb_events
    except Exception as e:
        raise RuntimeError(f"Failed to parse USB logs: {e}")
