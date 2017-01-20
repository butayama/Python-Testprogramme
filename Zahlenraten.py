geheimnis = 1337
versuch = 0
zaehler = 0
while versuch != geheimnis:
    versuch = int(input("Rate Zahl: "))
    if versuch < geheimnis:
        print("Zu klein")

    if versuch > geheimnis:
        print("Zu groß")

    zaehler += 1
print("in ", zaehler, "Versuchen")

    
