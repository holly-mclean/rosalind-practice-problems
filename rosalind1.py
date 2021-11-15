a = 0
c = 0
g = 0
t = 0

# Open file and read each char
with open("rosalind_dna.txt", "r") as file:
  for line in file:
    for ch in line:
      if ch == "A":
        a = a + 1
      if ch == "C":
        c = c + 1
      if ch == "G":
        g = g + 1
      elif ch == "T":
        t = t + 1

file.close()

print("%d %d %d %d" %(a, c, g, t))