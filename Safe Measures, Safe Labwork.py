print("Welcome to 'Safe Measures, Safe Labwork'")
risk_level = 0

chem = input("Are chemicals being used? (yes/no): ").lower()
heat = input("Will heat be used? (yes/no): ").lower()
flame = input("Will an open flame be used? (yes/no): ").lower()
glass = input("Will glassware be used? (yes/no): ").lower()
elec = input("Will electricity be used? (yes/no): ").lower()

print()
print("Laboratory Risks: ")

if chem == "yes":
    print("WARNING: Chemical hazard detected. Wear safety goggles and appropriate protective equipment.")
    risk_level += 1

if heat == "yes":
    print("WARNING: Heat hazard detected. Handle hot materials carefully.")
    risk_level += 1

if flame == "yes":
    print("WARNING: Open flame detected. Keep flammable materials away from the flame.")
    risk_level += 1

if glass == "yes":
    print("WARNING: Glassware is being used. Handle glassware carefully and check for cracks.")
    risk_level += 1

if elec == "yes":
    print("WARNING: Electric material is being used. Keep liquids away from electrical equipment.")
    risk_level += 1

print()
print("Conclusion: ")

if risk_level == 0:
    print("No hazards detected. Always follow your teacher's laboratory instructions.")

elif risk_level <= 2:
    print("Safety Status: LOW RISK. Review the safety precautions before starting.")

else:
    print("Safety Status: HIGH RISK. Review all safety precautions and ask your teacher before proceeding.")
  
print()
print("Total hazards detected:", risk_level)
print("Have a Safe Laboratory Activity! See you next time!")
