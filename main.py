#!/usr/bin/env python3
import os
import shutil
import sys
import hashlib

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    src_path = os.path.join(os.path.dirname(__file__), "entry.png")
    dest_path = os.path.join(output_dir, "entry.png")
    
    shutil.copyfile(src_path, dest_path)
    
    with open(dest_path, "rb") as f:
        data = f.read()
        
    if not data.startswith(b'\x89PNG\r\n\x1a\n'):
        print("Error: Copied file does not start with PNG signature", file=sys.stderr)
        sys.exit(1)
        
    size = len(data)
    h = hashlib.sha256(data).hexdigest()[:12]
    print(f"Size: {size}, SHA256: {h}")

if __name__ == "__main__":
    main()
