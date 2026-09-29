#!/usr/bin/env python3
import hashlib, os, sys
root = sys.argv[1]
for dp, _, fs in os.walk(root):
    for f in sorted(fs):
        p = os.path.join(dp, f)
        print(hashlib.sha256(open(p, "rb").read()).hexdigest(), p)
