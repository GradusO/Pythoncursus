servers ={}

while True:

    servernaam = input("Geef een servernaam? ")
    ip = input("Wat is het ip adres? ")
    servers[servernaam] = ip
    print(servers)
    nogeenwaarde = input("Continue (y/n)")
    if nogeenwaarde == "n":
        break

