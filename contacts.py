import sys
from faker import Faker
fake = Faker()

template = """BEGIN:VCARD
VERSION:2.1
N:{1};{0};;;
FN: {0} {1}
SOUND; X-IRMC-N:;;;;
TEL;CELL:{2}-{3}-{4:04d}
END:VCARD
"""

def name():
    n = fake.name()
    nargs = n.split(' ')
    if nargs[0] in ["Mrs.","Ms.","Miss","Dr.","Mr."]:
        del nargs[0]

    return nargs[0], nargs[1]

try:
    npa = int(sys.argv[1])
except IndexError:
    sys.exit()
nxx = 200
xxxx = 0000

f = open('{}_contacts.vcf'.format(npa),'w')

while npa == int(sys.argv[1]):
    npal = list(str(npa))
    if npal[1] == '9':
        npa += 1
        continue
    nxx = 200

    while nxx <= 999:
        nxxl = list(str(npa))
        if nxxl[1] == '1' and nxxl[2] == '1':
            nxx += 1
            continue
        if nxx == 555:
            nxx += 1
            continue

        xxxx = 0
        while xxxx <= 9999:
            first, last = name()
            e = template.format(first, last, npa, nxx, xxxx)
            print("  {}-{}-{:04d}\r".format(npa, nxx, xxxx), end="")
            f.write(e)
            xxxx += 1

        nxx += 1

    npa += 1
