
file = open("rosalind_ini5.txt", "r")

with file as infile:
    lines = infile.readlines()
    for line in lines:
        print(line.strip())

for l in lines[1::2]:
    print(l.strip())