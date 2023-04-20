# import csv
#
# try:
#     vlan = int(input("Vlan number? "))
#
#     matching = False
#
#     with open("interfaces.csv") as f:
#         f.readline() # skip header
#         r = csv.reader(f)
#         for server in r:
#             if int(server[1]) == vlan:
#                 matching = True
#                 print(f"interface {server[1]}")
#                 print(f"ip address {server[2]} {server[4]}")
#                 print("-----\n\n")
#
#     if not matching:
#         print("No matching lines")
# except ValueError:
#     print("That is not a valid number.")

# Oplossing love gemaakt in de les door tutor
import csv


vlan = input("Geef een vlan nummer?")

with open("interfaces.csv") as f:
    reader = csv.reader(f)

    vlan_gevonden = False

    for server in reader:
        if server[1] == vlan:
            print("interface", server[0])
            print("ip adress", server[2], server[4])
            vlan_gevonden = True


if not vlan_gevonden:
    print("Geen match")