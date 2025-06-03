# cli.py
import argparse
from forensics import usb_parser, browser_parser, metadata_parser, simulator

def main():
    parser = argparse.ArgumentParser(description="Digital Forensics Toolkit")
    parser.add_argument('--usb', help="Path to USB log file")
    parser.add_argument('--history', help="Path to Chrome history file")
    parser.add_argument('--file', help="Path to file for metadata")
    parser.add_argument('--simulate', action='store_true', help="Run investigation simulation")

    args = parser.parse_args()

    if args.usb:
        print("🔍 USB Log Events:")
        events = usb_parser.parse_usb_logs(args.usb)
        for e in events:
            print(e.strip())

    if args.history:
        print("\n🔍 Browser History (Top 10):")
        for url, title, visits in browser_parser.parse_chrome_history(args.history):
            print(f"{title} ({url}) - Visited {visits} times")

    if args.file:
        print("\n🔍 File Metadata:")
        meta = metadata_parser.extract_file_metadata(args.file)
        for k, v in meta.items():
            print(f"{k}: {v}")

    if args.simulate:
        print("\n🧪 Simulated Investigation Steps:")
        for step in simulator.simulate_investigation():
            print(step)

if __name__ == "__main__":
    main()
