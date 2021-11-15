rnaString = ""

# Open file and read each char
with open("rosalind_rna.txt", "r") as file:
  for line in file:
    for ch in line:
      if ch == "T":
        rnaString = rnaString + "U"
      else:
        rnaString = rnaString + ch

file.close()

print(rnaString)