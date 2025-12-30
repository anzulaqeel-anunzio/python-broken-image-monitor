# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from monitor.core import BrokenImageMonitor

def main():
    parser = argparse.ArgumentParser(description="Broken Image Link Monitor (Local)")
    parser.add_argument("path", help="Directory or file to scan (defaults to current dir)", nargs='?', default=".")
    
    args = parser.parse_args()
    path = os.path.abspath(args.path)
    
    issues = []
    
    if os.path.isfile(path):
        # Scan file, assuming its dir is root? Or purely relative check.
        # Ideally user provides root.
        issues = BrokenImageMonitor.scan_file(path, os.path.dirname(path))
    elif os.path.isdir(path):
        issues = BrokenImageMonitor.scan_directory(path)
    else:
        print(f"Error: Path '{path}' not found.")
        sys.exit(1)
        
    if not issues:
        print("Success! All local image links point to valid files.")
        sys.exit(0)
        
    print(f"Found {len(issues)} broken image links:\n")
    for issue in issues:
        print(f"[{issue['file']}:{issue['line']}] {issue['msg']}")
        
    sys.exit(1)

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
