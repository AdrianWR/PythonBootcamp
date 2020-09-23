#!/usr/bin/python3
from time import sleep
import time
import sys


def ft_progress(listy):
    width = 20
    size = len(listy)
    start_time = time.time()
    for i in listy:
        x = int(width/size * (i + 1))
        pct = int((i+1)/size*100)
        elapsed_time = time.time() - start_time
        eta = round(elapsed_time / (i+1) * size - elapsed_time, 2)
        sys.stdout.write(f"\rETA: {eta:.2f} s ")
        sys.stdout.write(f"[{pct:>3}%]")
        sys.stdout.write(f"[{'='*x+'>': <{width+1}}]")
        sys.stdout.write(f" | {i+1}/{len(listy)} | ")
        sys.stdout.write(f"elapsed time {elapsed_time:.2f} s")
        sys.stdout.flush()
        yield i


listy = range(100)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.1)
print()
print(ret)
