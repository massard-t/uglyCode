#!/usr/bin/env python
import sys,os
def hey(avar):return 1
def main():
    try:
        os.system(sys.argv[1:])
    except IndexError:
        print("No problem :)")
def yy(notavar):
    m = notavar
    print(m)
if __name__ == '__main__': main()
