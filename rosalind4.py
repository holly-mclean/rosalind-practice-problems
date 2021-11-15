# n = months
# k = number of rabbit pairs
# return: Fn: total number of rabbit pairs present after n months if we begin with 1 pair, and in each generation, every pair
#   of reproductive age rabbits produces a litter of k rabbit pairs

import sys

numArg = len(sys.argv)

if numArg < 3:
  print("need args!")
else:
  # Get data from command line
  months = int(sys.argv[1])
  factor = int(sys.argv[2])

  # FIBONACCI vanilla (1 1 2 3 5 8 13 19)
  print("1")  # always starts with 1

  #  fPrev   f    sum
  #    1     1     2     3     5
  f = 1
  fPrev = 0
  sum = 0
  months = months - 1

  # Run through once to get the second "1", and THEN enter the loop
  sum = f + fPrev
  fPrev = f
  f = sum
  print(sum)
  months = months - 1

  # h is the second multiplication factor and always starts at 1
  h = 1

  while months > 0:
    # Add the multiplication factors into the mix
    sum = (factor * h) + 1
    h = h + f
    fPrev = f
    f = sum

    print(sum)
    months = months - 1