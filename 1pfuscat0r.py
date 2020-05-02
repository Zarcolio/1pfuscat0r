#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import re, random
import sys
import signal

__version__ = '0.1'

def SignalHandler(sig, frame):
    # Create a break routine:
    print("\nCtrl-C detected, exiting...\n")
    sys.exit(1)

def GetArguments():
    # Get some commandline arguments:
    argParser=argparse.ArgumentParser(description='Use 1pfuscat0r to obfuscate a given IP address. Either supply an IP address as an argument or through standard input. By default valid and invalid IP addresses are shown.')
    argParser.add_argument('-i', metavar="<ipaddress>", help='Supply a valid IP address to obfuscate')
    argParser.add_argument('-o', metavar="<file>", help='Supply an output file')
    return argParser.parse_args()

def ValidateIpAddress(sIpAddress):
    sMatch = re.match('\A((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\Z',sIpAddress)
    if not sMatch:
        print ("The supplied IP address could not be validated, exting...\n")
        return False
    else:
        return True

def PrintObfuscatedAddresses(sIpAddress):
    sRandomHex = ""
    sRandomOct = ""
    sRandomBase = []
    iCount = 0
    lEverything = []

    lParts = sIpAddress.split('.')
    
    sZeroedParts = lParts[0] + "."
    for j in range(1, 4):
        iRandom = random.randint(0,5)
        if j < 3: sDot = "."
        else: sDot = ""
        
        sZeroedParts += "0" * iRandom + lParts[j] + sDot
        
    lEverything.append(sZeroedParts)

    iDecimal = int(lParts[0]) * 16777216 + int(lParts[1]) * 65536 + int(lParts[2]) * 256 + int(lParts[3])

    lHexlParts = []
    lOctlParts = []
    for i in lParts:
        lHexlParts.append(hex(int(i)))
        lOctlParts.append(oct(int(i)))

    for i in lHexlParts:
        sRandomHex += i.replace('0x','0x' + '0' * random.randint(1,30)) + '.'

    sRandomHex = sRandomHex[:-1]

    for i in lOctlParts:
        sRandomOct += '0' * random.randint(1,30) + i + '.'

    sRandomOct = sRandomOct[:-1]

    while iCount < 5:
        sRandomBaseEval = ""
        for i in range(0,4):
            val = random.randint(0,2)
            if val == 0:
                # dec
                sRandomBaseEval += lParts[i] + '.'
            elif val == 1:
                # hex
                sRandomBaseEval += lHexlParts[i] + '.'
            else:
                sRandomBaseEval += lOctlParts[i] + '.'
                # oct
        sRandomBase.append(sRandomBaseEval[:-1])
        lEverything.append(sRandomBase[iCount])
        iCount += 1

    sRandomBase = []
    iCount = 0
    
    while iCount < 5:
        sRandomBaseEval = ""
        for i in range(0,4):
            val = random.randint(0,2)
            if val == 0:
                # dec
                sRandomBaseEval += lParts[i] + '.'
            elif val == 1:
                # hex
                sRandomBaseEval += lHexlParts[i].replace('0x', '0x' + '0' * random.randint(1,30)) + '.'
            else:
                sRandomBaseEval += '0' * random.randint(1,30) + lOctlParts[i] + '.'
                # oct
        sRandomBase.append(sRandomBaseEval[:-1])
        lEverything.append(sRandomBase[iCount])
        iCount += 1    

    # Substitute numbers with encircled Unicode numbers:
    sIpAddressEncircled = sIpAddress
    sIpAddressEncircledPart1 = lParts[0]
    
    for c in range(0, 9):
        cc = c + 2460
        sIpAddressEncircled = sIpAddressEncircled.replace(str(c+1), (b'\\u%d' % cc).decode('raw_unicode_escape'), 9)
        
        sIpAddressEncircledPart1 = sIpAddressEncircledPart1.replace(str(c+1), (b'\\u%d' % cc).decode('raw_unicode_escape'), 9)

    sIpAddressEncircled = sIpAddressEncircled.replace("0", (b'\\u24EA').decode('raw_unicode_escape'), 9)

    # Randomize which numbers are replace with encircled ones:
    sIpAddressEncircledRandom = sIpAddress
    for c in range(0, 9):
        cc = c + 2460
        
        if bool(random.randint(0, 1)):
            sIpAddressEncircledRandom = sIpAddressEncircledRandom.replace(str(c+1), (b'\\u%d' % cc).decode('raw_unicode_escape'), 1)

    if bool(random.randint(0, 1)):
        sIpAddressEncircledRandom = sIpAddressEncircledRandom.replace("0", (b'\\u24EA').decode('raw_unicode_escape'), 1)

    sFirstHex = lHexlParts[0] + "." + lParts[1] + "." + lParts[2] + "." + lParts[3]
    sFirstOct = lOctlParts[0] + "." + lParts[1] + "." + lParts[2] + "." + lParts[3]
        
    lEverything.append (iDecimal)
    lEverything.append (str(sIpAddress).replace(".0", ""))
    if str(sIpAddress).count(".0") == 2: lEverything.append (str(sIpAddress).replace(".0", "", 1))
    lEverything.append (hex(iDecimal))
    lEverything.append (oct(iDecimal))
    lEverything.append ('.'.join(lHexlParts))
    lEverything.append('.'.join(lOctlParts))
    lEverything.append(sRandomHex)
    lEverything.append(sRandomOct)
    lEverything.append(sFirstHex)
    lEverything.append(sFirstOct)
    lEverything.append(str(sFirstHex).replace(".0", ""))
    if str(sFirstHex).count(".0") == 2: lEverything.append(str(sFirstHex).replace(".0", "", 1))
    lEverything.append(str(sFirstOct).replace(".0", ""))
    if str(sFirstOct).count(".0") == 2: lEverything.append(str(sFirstOct).replace(".0", "", 1))
    lEverything.append(sIpAddressEncircled)
    lEverything.append(sIpAddressEncircledPart1 + "." + lParts[1] + "." + lParts[2] + "." + lParts[3])
    lEverything.append(sIpAddressEncircledRandom)
    lEverything.append("[0:0:0:0:0:ffff:" + sIpAddress + "]")
    lEverything.append("[::ffff:" + sIpAddress + "]")
    lEverything.append("[0:0:0:0:0:ffff:" + hex(iDecimal) + "]")
    lEverything.append("[::ffff:" + hex(iDecimal) + "]")
    lEverything.append("[0:0:0:0:0:ffff:" + oct(iDecimal) + "]")
    lEverything.append("[::ffff:" + oct(iDecimal) + "]")


    if lArgs.o:
        fOut = open(lArgs.o, 'w', buffering=1)
        
    for sItem in lEverything:
        print(sItem)
        if lArgs.o:
            fOut.write(str(sItem) + "\n")

lArgs = GetArguments()
    
def main():
    signal.signal(signal.SIGINT, SignalHandler)
    if lArgs.i:
        if not ValidateIpAddress(lArgs.i):
            exit(2)
        PrintObfuscatedAddresses(lArgs.i)
    else:
        for sIpAddress in sys.stdin:
            sIpAddress = sIpAddress.strip()
            if not ValidateIpAddress(sIpAddress):
                continue
            PrintObfuscatedAddresses(sIpAddress)

if __name__ == '__main__':
    main()