# defining the DNA Sequences
rosalind_6404 = "CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG"
rosalind_5959 = "CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC"
rosalind_0808 = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"


# determining C content of rosalind_6404

{
rosalind_6404C = 0
for base in r1:
    if base == "C":
        rosalind_6404C = rosalind_6404C + 1

print(rosalind_6404C)
}


# determining G content of rosalind_6404

{
rosalind_6404G = 0
for base in r1:
    if base == "G":
        rosalind_6404G = rosalind_6404G + 1

print(rosalind_6404G)
}


# Total GC content of rosalind_6404

rosalind_6404GC = rosalind_6404G + rosalind_6404GC

print(rosalind_6404GC)

# Total number of base sequence of rosalind_6404

rosalind_6404_total = len(rosalind_6404)

# percentage of rosalind_6404 GC content

rosalind_6404GC% = (rosalind_6404GC / rosalind_6404_total ) * 100

# Repeat this for the other 2 sequences
# print the id and total gc% of the sequence with the highest GC%



