import re
portlist = open('PortNumbers.txt')
ergebnis = open('BelegtePorts.txt', 'w')
for line in portlist:
    ports = re.findall(r'\d{2,5}', line)
    # print(ports)
for i in range(0, 1):
    ergebnis.write(ports[i])
# TODO  Ausgabe korrigieren

