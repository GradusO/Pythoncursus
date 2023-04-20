count = 0
total_length = 0

with open("athletes.csv") as f:
    for line in f:
        fields = line.split(",")
        if fields[2] == '"female"':
            length_field = fields[3].replace('"', '')
            if length_field:
                total_length += float(length_field)
                count += 1

print(count, "women, with an average length of", str(total_length / count))

