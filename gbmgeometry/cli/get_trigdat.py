#!/usr/bin/env python

import sys
from gbmgeometry.io.data_download import download_trigdat

def main():
    """Entry point for get_trigdat command."""
    if len(sys.argv) != 2:
        print("Usage: get_trigdat <trigger_name>")
        sys.exit(1)
    
    bn = sys.argv[1]
    download_trigdat(bn)

if __name__ == "__main__":
    main()
