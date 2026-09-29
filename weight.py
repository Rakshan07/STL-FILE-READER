import os
import trimesh

# ===== SETTINGS =====
folder = r"C:\Users\raksh\OneDrive\Desktop\STL WEIGHING"

# PLA density (g/cm³)
density = 1.24

total_weight = 0

print(f"{'File Name':40} {'Weight (g)':>12}")

for file in os.listdir(folder):
    if file.lower().endswith(".stl"):
        path = os.path.join(folder, file)

        mesh = trimesh.load(path)

        volume_cm3 = mesh.volume / 1000  # mm³ → cm³
        weight = volume_cm3 * density

        total_weight += weight

        print(f"{file:40} {weight:10.2f}")

# Display total weight and price
print("\n" + "-" * 55)
print(f"Total Weight : {total_weight:.2f} g")

price = total_weight * 3
print(f"Total Price  : ₹{price:.2f}")