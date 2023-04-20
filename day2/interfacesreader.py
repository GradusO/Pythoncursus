import csv

with open("interfaces.csv") as f:
    f.readline() # skip header
    r = csv.reader(f)
    for server in r:
        print(f"interface {server[1]}")
        print(f"ip address {server[2]} {server[4]}")
        print("-----\n")