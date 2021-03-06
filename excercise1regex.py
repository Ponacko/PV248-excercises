from collections import Counter
import re
from math import floor

piecesByComposer = Counter()
piecesInCentury = Counter()
piecesInCMinor = Counter()
f = open('scorelib.txt', encoding="utf8")
r = re.compile(r"Composer: (.*)")
r2 = re.compile(r"Composition Year: (.*)")
r3 = re.compile(r"Key: (.*)")
for line in f:
    m = r.match(line)
    m2 = r2.match(line)
    m3 = r3.match(line)
    if m is not None:
        piecesByComposer[m.group(1)] += 1
    if m3 is not None and 'c minor' in m3.group(1):
        piecesInCMinor[0] +=1
    if m2 is not None:
        yearStr = m2.group(1).strip()
        if yearStr:
            if 'century' in yearStr or '.' in yearStr:
                piecesInCentury[yearStr[:2]] += 1
            else:
                try:
                    year = int(yearStr.split(' ')[0])
                    piecesInCentury[floor((year-1)/100 + 1)] += 1
                except ValueError:
                    continue
for k, v in piecesByComposer.items():
    print("%s composed %s pieces." % (k.rstrip(), v))
for k, v in piecesInCentury.items():
    print("There were %s pieces composed in the %sth century." % (v, k))
print("There were %s pieces composed in C minor." % (piecesInCMinor[0]))
