#!/usr/bin/env python
"""A nice module"""
import sys
import subprocess


def hey():
    """Returns 1"""
    return 1


def main():
    """Main function"""
    try:
        subprocess.call(sys.argv[1:])
        # os.system(sys.argv[1:])
    except IndexError:
        print("No problem :)")


def yy(notavar):
    myvar = notavar
    print(myvar)


if __name__ == '__main__': main()
