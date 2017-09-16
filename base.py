#!/usr/bin/env python
"""A nice module"""
import sys
import os


def hey(avar):
    return 1


def main():
    try:
        os.system(sys.argv[1:])
    except IndexError:
        print("No problem :)")


def yy(notavar):
    myvar = notavar
    print(myvar)


if __name__ == '__main__': main()
