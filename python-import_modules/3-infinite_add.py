#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    x = 0
    y = len(argv)
    for i in range(1, y):
        x += int(argv[i])
    print(f"{x}")
