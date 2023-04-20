filename = input("filename ?")

with open(filename) as f:
    with open(filename + "_filtered", "w") as fout:
        for line in f:
            line = line.replace("a", "o")
            fout.write(line)

