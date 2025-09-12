#!/usr/bin/env python

import sys
from gbmgeometry.io.data_download import download_posthist

def main():
    """Entry point for get_posthist command."""
    if len(sys.argv) != 4:
        print("Usage: get_posthist <year> <month> <day>")
        sys.exit(1)
    
    year, month, day = sys.argv[1:]
    download_posthist(year, month, day)

if __name__ == "__main__":
    main()
