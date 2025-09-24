# Simple stress calculator using load and area
load = 500  # Newtons
area = 50 * 10  # mm² (width * thickness)

stress = load / area

if stress < 50:
    print(f"Stress = {stress:.2f} MPa → Safe")
elif 50 <= stress < 150:
    print(f"Stress = {stress:.2f} MPa → Caution")
else:
    print(f"Stress = {stress:.2f} MPa → Failure Risk")

# output :
# Stress = 1.00 Mpa → Safe
