#!/usr/bin/env python

import sys
import random

def process_and_clear(pairs_buffer):
    pairs_buffer.sort()
    identifiers = [identifier for _, identifier in pairs_buffer]
    for _ in range(50):
        print(','.join(random.sample(identifiers, random.randint(1, 5))))
    del pairs_buffer[:]

pairs = []
buffer_size = 10000

for line in sys.stdin:
    line = line.strip()
    random_number, identifier = line.split('\t', 1)
    pairs.append((float(random_number), identifier))

    if len(pairs) >= buffer_size:
        process_and_clear(pairs)


if pairs:
    process_and_clear(pairs)

