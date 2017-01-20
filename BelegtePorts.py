import re
portlist = open(Portliste.txt)
ergebnis = open(BelegtePorts.txt,w)
for line in portlist
    ports = re.findall(r'\d{2,5}',line)
    ergebnis.write(ports)
    

