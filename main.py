inputNum = float(input("Enter temperature: "))
inputLtr = input("Enter unit in F/f or C/c: ")

if inputLtr=="f" or inputLtr=="F":
  convertF = (inputNum - 32) / 1.8
  print(f"{inputNum}° in Fahrenheit is equivalent to {convertF}° Celsius.")
elif inputLtr=="c" or inputLtr=="C":
  convertC = (inputNum *1.8) + 32
  print(f"{inputNum}° in Celsius is equivalent to {convertC}° Fahrenheit.")
else:
  print(f"Invalid unit({inputLtr}).")