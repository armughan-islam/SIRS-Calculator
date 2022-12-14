# The SIRS (Systemic Inflammatory Response Syndrome) score is calculated using
# body temperature, heart rate, respiratory rate and white cell count

print("Welcome to the SIRS score calculator.")
SIRS_score = 0

# Temperature

while True:
  temp = input("What is the patient's temperature? ")
  try:
    temp = float(temp)
  except ValueError:
    print("That is not a valid number. Please enter a number.")
    continue
  else:
    break

if (temp > 37.5) or (temp < 36.5):
  SIRS_score = SIRS_score + 1
  print("Points: ",SIRS_score)
else:
  print("The temperature is normal")
  print("Points: ",SIRS_score)

# Respiratory Rate

while True:
  respRate = input("What is the patient's repiratory rate? ")
  try:
    respRate = int(respRate)
  except ValueError:
    print("That was not a valid whole number. Please enter a number.")
    continue
  else:
    break
  
while True:
  paCO2 = input("What is the patient's PaCO2? (mmHg) ")
  try:
    paCO2 = int(paCO2)
  except ValueError:
    print("That was not a valid whole number. Please enter a number.")
    continue
  else:
    break

print("The respiratory rate is ", respRate, "and the PaCO2 is ", paCO2)

if respRate > 20 or paCO2 < 35:
  SIRS_score = SIRS_score + 1
  print("Points: ",SIRS_score)
else:
  print("The respiratory rate and the PaCO2 is normal")
  print("Points: ",SIRS_score)

# Heart Rate

while True:
  heartRate = input("What is the patient's heart rate? ")
  try:
    heartRate = int(heartRate)
  except ValueError:
    print("That was not a valid whole number. Please enter a number.")
    continue
  else:
    break

print("The heart rate is ", heartRate)

if heartRate > 90:
  SIRS_score = SIRS_score + 1
  print("Points: ",SIRS_score)
else:
  print("The heart rate is normal")
  print("Points: ",SIRS_score)

# White Cell Count

while True:
  wcc = input("What is the patient's white blood cell count? (x10^9/L) ")
  try:
    wcc = float(wcc)
  except ValueError:
    print("That was not a valid whole number. Please enter a number.")
    continue
  else:
    break

print("The white cell count is ", wcc, "x10^9/L")

if wcc > 12 or wcc < 4:
  SIRS_score = SIRS_score + 1
  print("Points: ",SIRS_score)
else:
  print("The white cell count is normal")
  print("Points: ",SIRS_score)

# Report Final Result

print("The total SIRS score is ", SIRS_score)

if SIRS_score >=2:
  print("The criteria for SIRS are met. The patient has SIRS.")
else:
  print("The criteria are not met. The patient does not have SIRS.")

