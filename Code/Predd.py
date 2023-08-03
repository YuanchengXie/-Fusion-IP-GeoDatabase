#!/usr/bin/env python
# -*- coding:utf-8 -*-
from IPy import IP
import requests
import json
import re


# Convert dotted decimal string IP address to decimal integer IP
def ip2int(ip):
    ch3 = lambda x: sum([256 ** j * int(i) for j, i in enumerate(x.split('.')[::-1])])
    return ch3(ip)


# Convert decimal integer IP to dotted decimal string IP address
def int2addr(dec):
    return ".".join([str(dec >> x & 0xff) for x in [24, 16, 8, 0]])


# Integrity check of IP address
def Integrity(filename):
    flag = 0
    f = open(filename, 'r', encoding='utf-8')
    line = f.readline().strip('\n')
    line = line.split('|')
    eip = line[1]
    line = f.readline().strip('\n')
    while line != '':
        line = line.split('|')
        sip = line[0]
        if ip2int(sip) != ip2int(eip) + 1:
            flag += 1
            print(sip, eip)
        eip = line[1]
        line = f.readline().strip('\n')
    print(flag)
    f.close()


# Integrity padding of network segments
def full_inty(filename):
    new_file = filename.split('.')[0] + '_1' + '.txt'
    f = open(filename, 'r', encoding='utf-8')
    f2 = open(new_file, 'w', encoding='utf-8')
    line = f.readline().strip('\n')
    f2.write(line + '\n')
    line = line.split('|')
    eip = line[1]
    line = f.readline().strip('\n')
    while line != '':
        res = line.split('|')
        sip = res[0]
        if ip2int(sip) != ip2int(eip) + 1:
            ins = '|'.join([int2addr(ip2int(eip)+1), int2addr(ip2int(sip)-1), '', '', '']) + '\n'
            f2.write(ins)
        eip = res[1]
        f2.write('|'.join(res) + '\n')
        line = f.readline().strip('\n')
    f.close()
    f2.close()


# Get the content of the specified field in the file
def segobt(filename, loc, outfile='output.txt'):
    f1 = open(filename, 'r')
    f2 = open(outfile, 'w', encoding='utf-8')
    line = f1.readline().strip('\n')
    res = []
    while line != '':
        prv = line.split('|')[loc-1]
        line = f1.readline().strip('\n')
        if prv == '':
            continue
        res.append(prv)
    nprv = list(set(res))
    for i in nprv:
        line = i + '\n'
        f2.write(line)
    f1.close()
    f2.close()


if __name__ == '__main__':
    segobt('IPUU_sort.txt', 3, 'stand_prov.txt')