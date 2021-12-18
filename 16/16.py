#!/usr/bin/env python

import sys
import math
from collections import defaultdict

operations=[
    sum,
    math.prod,
    min,
    max,
    None,
    lambda x: 1 if x[0] > x[1] else 0,
    lambda x: 1 if x[0] < x[1] else 0,
    lambda x: 1 if x[0] == x[1] else 0
]

class BitStringReader:
    def __init__(self, s):
        self.s = s

    def extract(self, n):
        r = self.s[:n]
        self.s = self.s[n:]
        return(r)

    def read(self, n):
        return(int(self.extract(n),2))

    def eof(self):
        return(len(self.s) == 0)

def packetdecode(b):
    value = 0
    versionsum=b.read(3)
    type=b.read(3)
    if type==4:
        #literal decoding
        lastseen = False
        while not lastseen:
            lastseen = b.read(1) == 0
            value=value*16+b.read(4)
    else:
        subvalues = []
        id = b.read(1)
        if id == 0 :
            l = b.read(15)
            subb = BitStringReader(b.extract(l))
            while not subb.eof():
                subversionsum, subvalue = packetdecode(subb)
                versionsum+=subversionsum
                subvalues.append(subvalue)
        else:
            p = b.read(11)
            for _ in range(p):
                subversionsum, subvalue = packetdecode(b)
                versionsum+=subversionsum
                subvalues.append(subvalue)
        value = operations[type](subvalues)
    return(versionsum, value)

def decode(h):
    bitlen=str(len(h)*4)
    fmt = "{:0"+bitlen+"b}"
    b=BitStringReader(fmt.format(int(h,16)))
    return(packetdecode(b))

# explanation examples
print(decode("D2FE28"))
print(decode("38006F45291200"))
print(decode("EE00D40C823060"))

# p1 examples
print(decode("8A004A801A8002F478"))
print(decode("620080001611562C8802118E34"))
print(decode("C0015000016115A2E0802F182340"))
print(decode("A0016C880162017C3686B18A3D4780"))

# p2 examples
print(decode("C200B40A82"))
print(decode("04005AC33890"))
print(decode("880086C3E88112"))
print(decode("CE00C43D881120"))
print(decode("D8005AC2A8F0"))
print(decode("F600BC2D8F"))
print(decode("9C005AC2F8F0"))
print(decode("9C0141080250320F1802104A08"))

print(decode("E20D72805F354AE298E2FCC5339218F90FE5F3A388BA60095005C3352CF7FBF27CD4B3DFEFC95354723006C401C8FD1A23280021D1763CC791006E25C198A6C01254BAECDED7A5A99CCD30C01499CFB948F857002BB9FCD68B3296AF23DD6BE4C600A4D3ED006AA200C4128E10FC0010C8A90462442A5006A7EB2429F8C502675D13700BE37CF623EB3449CAE732249279EFDED801E898A47BE8D23FBAC0805527F99849C57A5270C064C3ECF577F4940016A269007D3299D34E004DF298EC71ACE8DA7B77371003A76531F20020E5C4CC01192B3FE80293B7CD23ED55AA76F9A47DAAB6900503367D240522313ACB26B8801B64CDB1FB683A6E50E0049BE4F6588804459984E98F28D80253798DFDAF4FE712D679816401594EAA580232B19F20D92E7F3740D1003880C1B002DA1400B6028BD400F0023A9C00F50035C00C5002CC0096015B0C00B30025400D000C398025E2006BD800FC9197767C4026D78022000874298850C4401884F0E21EC9D256592007A2C013967C967B8C32BCBD558C013E005F27F53EB1CE25447700967EBB2D95BFAE8135A229AE4FFBB7F6BC6009D006A2200FC3387D128001088E91121F4DED58C025952E92549C3792730013ACC0198D709E349002171060DC613006E14C7789E4006C4139B7194609DE63FEEB78004DF299AD086777ECF2F311200FB7802919FACB38BAFCFD659C5D6E5766C40244E8024200EC618E11780010B83B09E1BCFC488C017E0036A184D0A4BB5CDD0127351F56F12530046C01784B3FF9C6DFB964EE793F5A703360055A4F71F12C70000EC67E74ED65DE44AA7338FC275649D7D40041E4DDA794C80265D00525D2E5D3E6F3F26300426B89D40094CCB448C8F0C017C00CC0401E82D1023E0803719E2342D9FB4E5A01300665C6A5502457C8037A93C63F6B4C8B40129DF7AC353EF2401CC6003932919B1CEE3F1089AB763D4B986E1008A7354936413916B9B080"))
