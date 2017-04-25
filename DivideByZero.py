def divideBy(divideBy):
  try:
    return 42/divideBy
  except ZeroDivisionError:
    print("Invalid argument")

print ("Program to check zeroDivisionError")
print(divideBy(42))
print(divideBy(0))
print(divideBy(12))
