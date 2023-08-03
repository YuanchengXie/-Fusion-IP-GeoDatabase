#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Convert dotted decimal string IP address to decimal integer IP
def ip2int(ip):
    ch3 = lambda x: sum([256 ** j * int(i) for j, i in enumerate(x.split('.')[::-1])])
    return ch3(ip)


# Convert decimal integer IP to dotted decimal string IP address
def int2addr(dec):
    return ".".join([str(dec >> x & 0xff) for x in [24, 16, 8, 0]])


# Compare geographic information, return consistent information and locate correct information
def geocomp(lists):
    legal = []
    flag = 1
    count = 0
    geo = []
    for i in range(0, len(lists)):
        li = lists[i]
        sign = 0
        if li[2] != '' and li[2] != '0':
            sign += 4
        if li[3] != '' and li[3] != '0':
            sign += 2
        if li[4] != '' and li[4] != '0':
            sign += 1
        if sign == 7:
            legal.append(li)
        elif sign == 0:
            count += 1
    if len(legal) == 0:
        if count == len(lists):
            flag = -1
        else:
            flag = 0
    else:
        for i in range(2, 5):
            geo.append(legal[0][i])
        for i in range(1, len(legal)):
            for j in range(0, 3):
                '''For example, Fujian and Fujian Province have the same geographic location, and simply using '==' to judge is a wrong judgment. In fact, it is best to use natural language analysis, but the difficulty is relatively high. Here, using the inclusion relationship to judge can also achieve the effect we are after.'''

                if geo[j] not in legal[i][j + 2] and legal[i][j + 2] not in geo[j]:
                    flag = 0
    return flag, geo


# Get the minimum value of the IP at the end of each line, and compare the consistency of geographic information.

def ipcomp(lines):
    lists = []
    for i in lines:
        lists.append(i.split('|'))

    # Let all start parameters be equal to the corresponding values of the first file.


    eip = lists[0][1]

    # Find the smallest last ip and compare whether the geographic information is consistent.
    for i in range(1, len(lists)):
        if ip2int(eip) > ip2int(lists[i][1]):
            eip = lists[i][1]
    flag, geo = geocomp(lists)
    return eip, flag, geo


# Process incoming offline library files.
def mergebase(files):
    handlef = []


    line = []

    # Create/Empty IPSame.txt and IPClush.txt
    f1 = open('IPSame.txt', 'w')
    f1.close()
    f2 = open('IPClush.txt', 'w')
    f2.close()
    for i in files:
        f = open(i, 'r', encoding='utf-8')
        handlef.append(f)
        line.append(f.readline().strip('\n'))
    file_num = len(handlef)
    while 1:
        eip, flag, geo = ipcomp(line)
        if flag == 1 or flag == -1:
            chag = same(line, eip, geo)
        else:
            chag = clush(line, eip)

    # Replace the fields that need to be replaced.
        for i in chag:
            line[i] = handlef[i].readline().strip('\n')

    # Judging whether the processing is complete.
        end = 0
        for k in line:
            if k == '':
                end += 1
        if end == file_num:
            Break

        # Close the offline library file.
        for i in handlef:
            i.close()


# When geolocation information matches.
def same(lines, eip, geo):
    # Corrected contrast segment.
    lists = []
    change = []
    for i in lines:
        lists.append(i.split('|'))


    flag = 0

    # Write consistent geographic information to IPSame.txt;
    if len(geo) != 0:
        f = open('IPSame.txt', 'a', encoding='utf-8')
        res = '|'.join([lists[0][0], eip, geo[0], geo[1], geo[2]]) + '\n'

        # shortest identical segment.
        f.write(res)
        f.close()
    for i in lists:
        if ip2int(eip) + 1 > ip2int(i[1]):
            change.append(flag)
        i[0] = int2addr(ip2int(eip) + 1)
        lines[flag] = '|'.join(i)
        flag += 1

    return change


# When the location information does not match.
def clush(lines, eip):
    f = open('IPClush.txt', 'a', encoding='utf-8')
    lists = []
    change = []
    res = ''
    backup = []
    for i in lines:
        lists.append(i.split('|'))
    flag = 0
    for i in lists:
        if ip2int(eip) + 1 > ip2int(i[1]):
            res = '|'.join([i[0], i[1]])
            change.append(flag)
        backup.append('|'.join([i[2], i[3], i[4]]))
        i[0] = int2addr(ip2int(eip) + 1)
        lines[flag] = '|'.join(i)
        flag += 1
    seg = [res]
    seg.extend(backup)
    res = '|'.join(seg) + '\n'
    f.write(res)
    f.close()
    return change

# ipcomp function function test.
"""
def test():
    files = ['IP2Region.txt', 'IPUU_sort.txt']
    handlef = []
    line = []
    for i in files:
        f = open(i, 'r', encoding='utf-8')
        line.append(f.readline().strip('\n'))
        handlef.append(f)
    eip, flag = ipcomp(line)
    chag = same(line, eip)
    for i in chag:
        line[i] = handlef[i].readline().strip('\n')
    print(line)
    # clush(line, eip)
    # print(line)
    for i in handlef:
        i.close()
"""

if __name__ == '__main__':
    files = ['IP2Region.txt', 'IPUU_sort.txt', 'GEOSecond.txt']
    mergebase(files)