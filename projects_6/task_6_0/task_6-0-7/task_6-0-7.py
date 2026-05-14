import pandas as pd

df = pd.read_csv('wild_boars.csv')

file = open('variation_values.txt', 'w')

variance = df['age_years'].var()
std = df['age_years'].std()
cv = std / df['age_years'].mean() * 100

file.write("age_years:\n")
file.write(f"Variance: {variance:.2f}\n")
file.write(f"Standard deviation: {std:.2f}\n")
file.write(f"Coefficient of variation: {cv:.2f}%\n\n")

variance = df['weight_kg'].var()
std = df['weight_kg'].std()
cv = std / df['weight_kg'].mean() * 100

file.write("weight_kg:\n")
file.write(f"Variance: {variance:.2f}\n")
file.write(f"Standard deviation: {std:.2f}\n")
file.write(f"Coefficient of variation: {cv:.2f}%\n\n")

variance = df['length_cm'].var()
std = df['length_cm'].std()
cv = std / df['length_cm'].mean() * 100

file.write("length_cm:\n")
file.write(f"Variance: {variance:.2f}\n")
file.write(f"Standard deviation: {std:.2f}\n")
file.write(f"Coefficient of variation: {cv:.2f}%\n\n")

variance = df['shoulder_height_cm'].var()
std = df['shoulder_height_cm'].std()
cv = std / df['shoulder_height_cm'].mean() * 100

file.write("shoulder_height_cm:\n")
file.write(f"Variance: {variance:.2f}\n")
file.write(f"Standard deviation: {std:.2f}\n")
file.write(f"Coefficient of variation: {cv:.2f}%\n\n")

variance = df['tusk_length_cm'].var()
std = df['tusk_length_cm'].std()
cv = std / df['tusk_length_cm'].mean() * 100

file.write("tusk_length_cm:\n")
file.write(f"Variance: {variance:.2f}\n")
file.write(f"Standard deviation: {std:.2f}\n")
file.write(f"Coefficient of variation: {cv:.2f}%\n\n")

variance = df['litter_size'].var()
std = df['litter_size'].std()
cv = std / df['litter_size'].mean() * 100

file.write("litter_size:\n")
file.write(f"Variance: {variance:.2f}\n")
file.write(f"Standard deviation: {std:.2f}\n")
file.write(f"Coefficient of variation: {cv:.2f}%\n\n")

variance = df['health_score'].var()
std = df['health_score'].std()
cv = std / df['health_score'].mean() * 100

file.write("health_score:\n")
file.write(f"Variance: {variance:.2f}\n")
file.write(f"Standard deviation: {std:.2f}\n")
file.write(f"Coefficient of variation: {cv:.2f}%\n\n")

variance = df['territory_ha'].var()
std = df['territory_ha'].std()
cv = std / df['territory_ha'].mean() * 100

file.write("territory_ha:\n")
file.write(f"Variance: {variance:.2f}\n")
file.write(f"Standard deviation: {std:.2f}\n")
file.write(f"Coefficient of variation: {cv:.2f}%\n\n")

file.close()

print("Файл создан")
