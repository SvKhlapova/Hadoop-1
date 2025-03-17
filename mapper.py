#!/usr/bin/env python

import sys
import random

for line in sys.stdin:
    line = line.strip()
    print("{}\t{}".format(random.random(), line))
