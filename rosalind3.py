dnaComplement = ""

# Open file and read each char
with open("rosalind_revc.txt", "r") as file:
  for line in file:
    for ch in line:
      if ch == "A":
        dnaComplement = dnaComplement + "T"
      if ch == "C":
        dnaComplement = dnaComplement + "G"
      if ch == "G":
        dnaComplement = dnaComplement + "C"
      elif ch == "T":
        dnaComplement = dnaComplement + "A"

file.close()

print(dnaComplement[::-1])